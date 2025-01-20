const puppeteer = require('puppeteer');

async function screenshotQuotes() {
  const browser = await puppeteer.launch();
  const page = await browser.newPage();
  await page.goto('file:///path/to/your/html/file.html'); // Replace with your file path. If it's online, use the URL.

  const quoteCount = await page.evaluate(() => {
    return document.querySelectorAll('.quote').length;
  });

  for (let i = 0; i < quoteCount; i++) {
    await page.click('#contenedor'); // Simulate click to advance the carousel.
    await page.waitForTimeout(500); // Small delay to ensure transition completes (adjust as needed)
    await page.screenshot({ path: `quote-${i + 1}.png` });
  }

  await browser.close();
}

screenshotQuotes();