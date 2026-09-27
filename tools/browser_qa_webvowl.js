// Render the committed offline bundle in a local Chromium session in CI.
// Screenshots remain private workflow artifacts; this does not deploy Pages.
const assert = require("node:assert/strict");
const fs = require("node:fs");
const path = require("node:path");
const { spawn } = require("node:child_process");
const { chromium } = require("playwright");

const root = path.resolve(__dirname, "..");
const bundle = path.join(root, "docs/ontology/generated/webvowl-viewer-candidate-v0.1");
const artifacts = path.join(root, "webvowl-browser-qa-artifacts");
const port = 18765;
const origin = `http://127.0.0.1:${port}`;
fs.mkdirSync(artifacts, { recursive: true });

async function ready() {
  for (let i = 0; i < 40; i++) {
    try {
      const response = await fetch(origin + "/");
      if (response.ok) return;
    } catch (_) { /* server is starting */ }
    await new Promise(resolve => setTimeout(resolve, 250));
  }
  throw new Error("Local HTTP server did not start");
}

async function inspect(browser, name, viewport) {
  const page = await browser.newPage({ viewport, deviceScaleFactor: 1 });
  const pageErrors = [];
  const outbound = [];
  const jsonResponses = [];
  page.on("pageerror", error => pageErrors.push(error.message));
  page.on("request", request => {
    if (!request.url().startsWith(origin + "/")) outbound.push(request.url());
  });
  page.on("response", response => {
    if (response.url().endsWith("/data/semrisk.json")) jsonResponses.push(response.status());
  });
  try {
    const response = await page.goto(origin + "/", { waitUntil: "domcontentloaded" });
    assert.equal(response.status(), 200);
    await page.waitForFunction(
      () => document.querySelectorAll("#graph svg.vowlGraph .nodeContainer .node").length >= 35,
      null, { timeout: 120000 }
    );
    await page.locator("#loading-info").waitFor({ state: "hidden", timeout: 120000 });
    await page.waitForTimeout(500);
    assert(!((await page.locator('meta[name="viewport"]').getAttribute("content")) || "").includes("user-scalable=no"), "browser pinch zoom disabled");
    const nodeCount = await page.locator("#graph svg.vowlGraph .nodeContainer .node").count();
    const graphBox = await page.locator("#graph svg.vowlGraph").boundingBox();
    assert(graphBox && graphBox.width > 250 && graphBox.height > 250);
    await page.waitForFunction(
      () => document.querySelector("#detailsArea").classList.contains("hidden"),
      null, { timeout: 10000 }
    );
    const canvasBox = await page.locator("#canvasArea").boundingBox();
    assert(canvasBox && canvasBox.width >= viewport.width - 2, "graph canvas is restricted by details rail");
    if (name === "mobile") {
      const overflow = await page.evaluate(() => ({
        scrollWidth: document.documentElement.scrollWidth,
        offenders: [...document.querySelectorAll("body *")].map(element => {
          const rect = element.getBoundingClientRect();
          return { tag: element.tagName, id: element.id, className: typeof element.className === "string" ? element.className : "", right: Math.round(rect.right), width: Math.round(rect.width) };
        }).filter(row => row.right > window.innerWidth + 3 && row.width > 0).slice(0, 12)
      }));
      console.log("MOBILE_OVERFLOW " + JSON.stringify(overflow));
      assert(overflow.scrollWidth <= viewport.width + 1, "mobile document overflows viewport");
    }
    assert(jsonResponses.includes(200), "local SemRisk JSON was not loaded");
    assert.equal(pageErrors.length, 0, JSON.stringify(pageErrors));
    assert.equal(outbound.length, 0, JSON.stringify(outbound));
    await page.locator("#search-input-text").fill("Risk");
    assert.equal(await page.locator("#search-input-text").inputValue(), "Risk");
    const before = await page.locator("#graph svg.vowlGraph > g").getAttribute("transform");
    const zoomButton = await page.locator("#zoomInButton").boundingBox();
    assert(zoomButton, "zoom button is not visible");
    await page.mouse.move(zoomButton.x + zoomButton.width / 2, zoomButton.y + zoomButton.height / 2);
    await page.mouse.down();
    await page.waitForTimeout(450);
    await page.mouse.up();
    await page.waitForTimeout(350);
    const after = await page.locator("#graph svg.vowlGraph > g").getAttribute("transform");
    assert.notEqual(after, before, "zoom control did not change graph transform");
    await page.locator("#semriskNotice a").first().click({ trial: true });
    const filterHint = page.locator('[id^="killFilterMessages_"]').first();
    if (await filterHint.count()) {
      await filterHint.click();
      await page.waitForTimeout(800);
    }
    await page.screenshot({ path: path.join(artifacts, `webvowl-${name}.png`), fullPage: false });
    console.log(JSON.stringify({ viewport: name, nodeCount, jsonResponses, outbound, pageErrors, zoom: "changed" }));
  } catch (error) {
    await page.screenshot({ path: path.join(artifacts, `webvowl-${name}-failure.png`), fullPage: false }).catch(() => {});
    throw error;
  } finally {
    await page.close();
  }
}

async function inspectModule(browser, slug, viewport) {
  const page = await browser.newPage({ viewport });
  const pageErrors = [];
  const outbound = [];
  const jsonResponses = [];
  page.on("pageerror", error => pageErrors.push(error.message));
  page.on("request", request => {
    if (!request.url().startsWith(origin + "/")) outbound.push(request.url());
  });
  page.on("response", response => {
    if (response.url().endsWith("/data/semrisk-" + slug + ".json")) jsonResponses.push(response.status());
  });
  try {
    await page.goto(origin + "/#semrisk-" + slug, { waitUntil: "domcontentloaded" });
    await page.waitForFunction(
      () => document.querySelectorAll("#graph svg.vowlGraph .nodeContainer .node").length > 0,
      null, { timeout: 60000 }
    );
    await page.locator("#loading-info").waitFor({ state: "hidden", timeout: 120000 });
    await page.waitForTimeout(500);
    await page.waitForFunction(
      () => document.querySelector("#detailsArea").classList.contains("hidden"),
      null, { timeout: 10000 }
    );
    assert(jsonResponses.includes(200), "module JSON was not loaded: " + slug);
    assert.deepEqual(pageErrors, [], slug);
    assert.deepEqual(outbound, [], slug);
    const nodes = await page.locator("#graph svg.vowlGraph .nodeContainer .node").count();
    if (slug === "enterprise") {
      await page.screenshot({ path: path.join(artifacts, "webvowl-enterprise.png"), fullPage: false });
    }
    console.log(JSON.stringify({ module: slug, visibleNodes: nodes, jsonResponses, outbound, pageErrors }));
  } catch (error) {
    await page.screenshot({ path: path.join(artifacts, "webvowl-module-" + slug + "-failure.png"), fullPage: false }).catch(() => {});
    throw error;
  } finally {
    await page.close();
  }
}

async function main() {
  const server = spawn("python3", ["-m", "http.server", String(port), "--bind", "127.0.0.1"], {
    cwd: bundle, stdio: "ignore"
  });
  let browser;
  try {
    await ready();
    browser = await chromium.launch({ headless: true });
    await inspect(browser, "desktop", { width: 1440, height: 900 });
    await inspect(browser, "mobile", { width: 390, height: 844 });
    for (const slug of ["core", "enterprise", "method", "governance", "pharma"]) {
      await inspectModule(browser, slug, { width: 1440, height: 900 });
    }
    console.log("SEM_RISK_WEBVOWL_RENDER_SMOKE_PASS | combined plus five module views; private offline Chromium; no public URL");
  } finally {
    if (browser) await browser.close();
    server.kill("SIGTERM");
  }
}

main().catch(error => { console.error(error); process.exitCode = 1; });
