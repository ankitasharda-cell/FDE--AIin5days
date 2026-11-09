# Daily Antigravity learning agent

This repository includes a GitHub Actions workflow that publishes a daily Antigravity learning digest at 09:00 UTC and posts it to a Google Chat space. Each digest includes a rotating hands-on learning prompt, official Antigravity resource links, and matching Antigravity mentions found in public Google developer feeds.

## Configure Google Chat

1. In the target Google Chat space, create an incoming webhook and copy its URL.
2. In this GitHub repository, open Settings → Secrets and variables → Actions.
3. Create a repository secret named `GOOGLE_CHAT_WEBHOOK_URL` and set its value to the webhook URL. Keep the URL secret; anyone with it may be able to post to the space.
4. Under Settings → Actions → General → Workflow permissions, allow read and write access to repository contents so the workflow can archive each digest.
5. Run Actions → Daily Antigravity learning digest → Run workflow to test it.

## Where to find the updates

Digest archives are committed to `daily-digests/`. The scheduled workflow runs every day at 09:00 UTC. GitHub Actions may start scheduled runs a little later during high load.

## Public feeds and resources

The agent checks these public feeds for entries mentioning Antigravity:
- Google Developers Blog Atom feed: https://developers.googleblog.com/atom.xml
- Google AI Blog RSS feed: https://blog.google/rss/

It also includes links to the Antigravity documentation, Getting Started codelab, and Building with Antigravity codelab.

Feed checks are best-effort. If a feed is unavailable, the learning prompt and resource links are still produced. Feed matching uses the word “Antigravity” and may not find every relevant update.
