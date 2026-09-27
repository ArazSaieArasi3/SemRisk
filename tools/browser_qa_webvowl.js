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
    await page.waitForTimeout(1500);
    const nodeCount = await page.locator("#graph svg.vowlGraph .nodeContainer .node").count();
    const graphBox = await page.locator("#graph svg.vowlGraph").boundingBox();
    assert(graphBox && graphBox.width > 250 && graphBox.height > 250);
    assert(jsonResponses.includes(200), "local SemRisk JSON was not loaded");
    assert.equal(pageErrors.length, 0, JSON.stringify(pageErrors));
    assert.equal(outbound.length, 0, JSON.stringify(outbound));
    await page.locator("#search-input-text").fill("Risk");
    assert.equal(await page.locator("#search-input-text").inputValue(), "Risk");
    const before = await page.locator("#graph svg.vowlGraph > g").getAttribute("transform");
    await page.locator("#zoomInButton").click();
    await page.waitForTimeout(800);
    const after = await page.locator("#graph svg.vowlGraph > g").getAttribute("transform");
    assert.notEqual(after, before, "zoom control did not change graph transform");
    await page.screenshot({ path: path.join(artifacts, `webvowl-${name}.png`), fullPage: true });
    console.log(JSON.stringify({ viewport: name, nodeCount, jsonResponses, outbound, pageErrors, zoom: "changed" }));
  } catch (error) {
    await page.screenshot({ path: path.join(artifacts, `webvowl-${name}-failure.png`), fullPage: true }).catch(() => {});
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
    console.log("SEM_RISK_WEBVOWL_RENDER_SMOKE_PASS | private offline Chromium; no public URL");
  } finally {
    if (browser) await browser.close();
    server.kill("SIGTERM");
  }
}

main().catch(error => { console.error(error); process.exitCode = 1; });
