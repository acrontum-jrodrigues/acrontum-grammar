const forbiddenProtocols = [
  "chrome-extension://",
  "chrome-search://",
  "chrome://",
  "devtools://",
  "edge://",
  "https://chrome.google.com/webstore",
];

export function isForbiddenUrl(url: string): boolean {
  return forbiddenProtocols.some((protocol) => url.startsWith(protocol));
}

export const isFirefox = navigator.userAgent.includes("Firefox");

export const webAppUrl =
  process.env.NODE_ENV !== "production"
    ? "http://localhost:5173"
    : "http://localhost:5173"; // FIXME: change to your web app url when prod environment is setup
