# Daily Antigravity digest

This GitHub Actions workflow emails a daily digest of news about Google's
Antigravity development platform at 9:00 a.m. Pacific time, including daylight
saving time. GitHub may delay scheduled runs. It searches Google News for
recent English-language headlines, asks Gemini to summarize those headlines,
and includes the original source links. The summaries are based on headlines,
not full articles, and the feed does not cover every update.

## Setup

In the repository's **Settings > Secrets and variables > Actions**, add these
repository secrets:

| Secret | Value |
| --- | --- |
| `GEMINI_API_KEY` | Google Gemini API key with access to `gemini-2.5-flash` |
| `SMTP_HOST` | SMTP server hostname |
| `SMTP_PORT` | SMTP port (optional; defaults to 587 for STARTTLS, or use 465 for implicit TLS) |
| `SMTP_USERNAME` | SMTP login |
| `SMTP_PASSWORD` | SMTP password or provider-specific app password |
| `SMTP_FROM` | Sender email address |
| `SMTP_TO` | Recipient email address |

Use an SMTP provider that permits authenticated sending. Never commit credentials.
After the workflow is on the default branch and the secrets are configured, use
**Actions > Daily Antigravity digest > Run workflow** to send a test email.
Scheduled workflows run only from the default branch and can be disabled by
GitHub after prolonged inactivity in a public repository.

If no recent headlines are found, the email says so. Feed, Gemini, and SMTP
errors fail the workflow rather than sending a misleading digest. Headlines are
sent to Gemini for summarization.
