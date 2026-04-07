# DeepThread — AI Cross-Platform Context Engine

**Status:** In Development (Product Hunt launch planned)
**Domain:** deepthread.ai
**Repo:** `Deepthread-website` (primary), `threadgpt` (earlier version)

---

## What It Is

An AI-powered tool that connects GitHub, Slack, Jira, Linear, Notion, and Google Docs — generating instant standups, handoff documents, and issue summaries. It eliminates manual reporting by automatically understanding context across platforms.

---

## Tech Stack (from `Deepthread-website` repo)

- **Framework:** Next.js 15 + React
- **UI:** ShadCN UI components + Tailwind CSS + Framer Motion
- **Database:** Drizzle ORM + Neon (serverless Postgres)
- **Auth:** Firebase (GitHub OAuth) + JWT + bcrypt
- **AI Models:** Anthropic Claude SDK + OpenAI + Google Gemini + Cohere (multi-model — picks best per task)
- **Email:** Nodemailer
- **Testing:** Cypress E2E
- **Forms:** React Hook Form + Zod
- **Payments:** Paystack (subscription management)

---

## App Structure (from codebase)

### API Routes (app/api/)
| Route | Purpose |
|-------|---------|
| `llm/` | Multi-model AI analysis endpoints |
| `jira-prokcy/` | Jira proxy for issue fetching |
| `confluence-prokcy/` | Confluence proxy for document fetching |
| `google/` | Google Docs/Drive integration |
| `transaction/` | Payment/subscription handling |
| `users/` | User management |
| `mail/` | Email notifications |
| `submit-form/` | Form submission handler |
| `webhook/` | Webhook receivers |
| `utils/` | Shared API utilities |

### Frontend Pages
| Route | Purpose |
|-------|---------|
| `/` | Landing page / marketing site |
| `/dashboard` | Main user dashboard |
| `/dashboard/login` | Dashboard authentication |
| `/payments` | Payment/subscription management |
| `/buy-callback` | Paystack payment callback |
| `/callback` | OAuth callback |
| `/get-more-page` | Upsell/upgrade page |
| `/privacypolicy` | Privacy policy |
| `/termofservices` | Terms of service |

### Components
- `customGoogleForm.tsx` — Custom Google form integration
- `navbar.tsx` — Navigation
- `logo.tsx` — Brand logo
- `theme-provider.tsx` / `theme-toggle.tsx` — Dark/light mode

---

## Core Capabilities

- Cross-platform context engine (GitHub + Slack + Jira + Linear + Notion + Google Docs + Confluence)
- Multi-model AI analysis (Claude, GPT, Gemini, Cohere)
- Instant standup generation from team activity
- One-click handoff document creation
- Issue summaries pulling context from multiple platforms simultaneously
- Predictive business automation
- Firebase auth with GitHub OAuth
- Paystack subscriptions for premium access

---

## Related Repos

### `threadgpt`
Earlier/simpler version of the same concept. Next.js + ShadCN UI setup. Appears to be the initial prototype before the full Deepthread-website build.

### `gh-issue-analyzer`
Chrome extension for AI-powered GitHub issue analysis. Related product — uses the same multi-AI approach (Gemini, Claude, Cohere). Includes:
- Chrome extension source (`src/`)
- Firebase Cloud Functions backend (`functions/`)
- Firebase hosting for auth (`hosting/`, `public-auth/`)
- Paystack subscription integration
- Webpack build config

### `analyzer-backend-new`
Next.js backend service for the analyzer. Includes:
- Drizzle ORM + Neon Postgres database
- Multi-AI endpoints (Gemini, Anthropic, Cohere)
- Cypress E2E tests
- Paystack payment handling
- Vercel deployment

---

## Target Users

Software developers, product managers, remote teams, engineering leads — anyone tired of context-switching and manual reporting.

## Product Hunt Positioning
"Instant standups & handoffs from GitHub, Slack, Jira" — Categories: Developer Tools, Productivity, AI, Remote Work

---

*Based on codebase analysis of `Deepthread-website`, `threadgpt`, `gh-issue-analyzer`, and `analyzer-backend-new` repos + Product_Context/DeepThread.md*
