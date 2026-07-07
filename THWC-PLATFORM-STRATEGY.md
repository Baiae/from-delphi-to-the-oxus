# Product Strategy: An All-in-One Digital Platform for the Transgender Health and Wellness Center (TH&WC)

**Prepared:** July 2026
**Scope:** Public-source strategic analysis and tailored platform design
**Status:** Pre-engagement strategy document — requires stakeholder validation before build

---

## How to read this document

This document was produced entirely from lawful, public, organization-level sources. It contains **no** information about individual clients, patients, donors, or community members, and no material from behind authentication. Every factual claim is either cited to a public source or explicitly labeled **[INFERENCE]** (a reasonable conclusion drawn from public evidence) or **[UNKNOWN]** (something only the organization can confirm). Staff are named only where the organization itself publicly lists them.

**Document map** (matching the requested final output structure):

| # | Requested output | Where it lives |
|---|---|---|
| 1 | Research methodology | Part A.1 |
| 2 | Source list | Part A.2 |
| 3 | Organization profile | Section 2 |
| 4 | Needs analysis | Sections 3–4 |
| 5 | Product vision | Section 6 |
| 6 | App modules | Section 7 |
| 7 | User journeys | Section 8 |
| 8 | Data model | Sections 9–10 |
| 9 | Privacy/security architecture | Section 11 |
| 10 | MVP | Section 13 |
| 11 | Roadmap | Section 14 |
| 12 | Budget/stack options | Sections 13 & 15–16 |
| 13 | Risk register | Section 18 |
| 14 | Validation plan | Section 19 |
| 15 | Final recommendation | Section 20 |
| 16 | Open questions for stakeholder interview | Section 20.6 |

---

# PART A — RESEARCH FOUNDATION

## A.1 Research methodology

**Approach.** Iterative public-source research conducted in July 2026, using web search across the organization's own website (trans.health), nonprofit transparency databases (ProPublica Nonprofit Explorer, GuideStar/Candid, Cause IQ, Charity Navigator), state regulatory records (California HCAI facility database, NPI registry), state grant program documentation (CDPH TGI Wellness and Equity Fund), local and regional news (KESQ, The Palm Springs Post, Gay Desert Guide), community resource directories (findhelp.org, LawHelpCA, City of Palm Springs resource lists), event platforms (Eventbrite), and volunteer-matching platforms (TurnOut, Idealist).

**Constraints encountered.** The organization's website (trans.health) could not be fetched directly from this research environment (network policy restrictions), so its content was reconstructed from search-index excerpts of specific trans.health pages (home, About Us, Our Team, Locations, Contact, Support Groups, Hair Removal Service, Insurance Navigation, Volunteer, Donate, event pages, and a public funding notice). This means some on-site details (full staff roster, exact intake instructions, complete support-group schedule) are cited at page level but not quoted in full. These are flagged as items to confirm in discovery.

**Ethical boundaries applied.**
- No attempt to access anything behind authentication; no private accounts, internal systems, or records.
- No collection or profiling of individual clients, patients, donors, volunteers, or community members.
- Public reviews were used only to understand *service categories offered* (e.g., that electrolysis is offered), never to characterize individuals.
- Staff discussed only where the organization or reputable press publicly lists them, and only as relevant to organizational needs.
- All community members who might use the proposed platform are treated as high-risk users from a privacy and safety standpoint throughout.

**Fact/inference discipline.** Claims are tagged: plain text with a citation = verified public fact; **[INFERENCE]** = reasoned conclusion from public evidence; **[UNKNOWN]** = requires stakeholder confirmation.

## A.2 Source list

Organization-owned sources (content accessed via search index excerpts):

1. TH&WC website home — https://trans.health/
2. About Us — https://trans.health/about-us/
3. Our Team — https://trans.health/our-team/
4. Our Locations — https://trans.health/locations/
5. Contact Us — https://trans.health/contact-us/
6. Support Groups — https://trans.health/resources/support-groups/
7. Hair Removal Service — https://trans.health/services/hair-removal-service/
8. Insurance Navigation — https://trans.health/services/insurance-navigation/
9. Volunteer — https://trans.health/volunteer/
10. Donate — https://trans.health/donate/
11. Trans Pride 2026 "Empower and Employ" event page — https://trans.health/thwc-event/trans-pride-2026-empower-and-employ/
12. Housing Program Notice Regarding Federal Funding — https://trans.health/notice/housing-program-notice-regarding-federal-funding/
13. Team page for founder — https://trans.health/team/thomi-clinton/
14. TH&WC Eventbrite organizer page — https://www.eventbrite.com/o/transgender-health-wellness-center-37769245893
15. Instagram — https://www.instagram.com/transhealthandwellnesscenter/
16. Facebook — https://www.facebook.com/TransHealthAndWellnessCenter/ and community group https://www.facebook.com/groups/TransCC/

Regulatory, transparency, and directory sources:

17. ProPublica Nonprofit Explorer, EIN 82-4659164 — https://projects.propublica.org/nonprofits/organizations/824659164
18. GuideStar/Candid profile — https://www.guidestar.org/profile/82-4659164
19. Cause IQ profile — https://www.causeiq.com/organizations/transgender-health-and-wellness-center,824659164/
20. Charity Navigator rating — https://www.charitynavigator.org/ein/824659164
21. California HCAI facility record (Community Clinic license) — https://hcai.ca.gov/facility/transgender-health-and-wellness-center/
22. NPI registry record 1639024938 (Clinic/Center, Oceanside, CA) — https://npiprofile.com/npi/1639024938
23. findhelp.org program listings (multiple counties) — e.g., https://www.findhelp.org/transgender-health-and-wellness-center-(th&c)--riverside-ca--mental-health-services/6098361049546752
24. LawHelpCA organization listing — https://www.lawhelpca.org/organization/transgender-health-and-wellness-center
25. TurnOut volunteer listing — https://www.turnout.org/vol-opps/the-transgender-health-and-wellness-center
26. Idealist listing — https://www.idealist.org/en/nonprofit/5c096445dbe44163b219b68f6549e964-transgender-health-wellness-center-palm-springs
27. Gay Desert Guide directory — https://gaydesertguide.com/directory-category/transgender-health-and-wellness-center/
28. Desert Business Association member listing — https://www.desertbusinessassociation.org/list/member/transgender-health-wellness-center-2025

Government funding context:

29. CDPH TGI Wellness and Equity Fund program page — https://www.cdph.ca.gov/Programs/OHE/Pages/TGIUnit.aspx
30. CDPH TGI Fund Community Care Grants RFA — https://www.cdph.ca.gov/Programs/OHE/CDPH%20Document%20Library/GHEU/TGI_Fund_Community_Care_Grants_Track1_RFA23-10732.pdf
31. AB 2218 (2020) Transgender Wellness and Equity Fund — https://leginfo.legislature.ca.gov/faces/billTextClient.xhtml?bill_id=201920200AB2218
32. State grant coverage — https://lachealthequity.substack.com/p/state-invests-in-community-organizations
33. Medi-Cal transgender services coverage (context for hair-removal billing) — https://providerlibrary.healthnetcalifornia.com/medi-cal/provider-manual/benefits/transgender-services-medi-cal.html and https://mcweb.apps.prd.cammis.medi-cal.ca.gov/news/33457

News coverage:

34. KESQ, "Local center expanding resources for transgender people, housing and food assistance" (Oct 10, 2024 — Healing Rainbows opening) — https://kesq.com/news/2024/10/10/local-center-offering-resources-for-transgender-people-housing-and-food-assistance/
35. KESQ, "Hundreds attend 2025 Palm Springs Trans Pride event" (Mar 29, 2025) — https://kesq.com/news/2025/03/29/hundreds-attend-2025-palm-springs-trans-pride-event/
36. KESQ, "HRC to honor Palm Springs, Transgender Health and Wellness Center" (Oct 7, 2025) — https://kesq.com/news/cv-questions-answered/2025/10/07/hrc-to-honor-palm-springs-transgender-health-and-wellness-center-at-annual-garden-party/
37. KESQ, "Palm Springs, Transgender Health and Wellness Center honored for LGBTQ+ equality advancements" (Nov 8, 2025) — https://kesq.com/news/2025/11/08/palm-springs-transgender-health-and-wellness-center-honored-for-work-in-lgbtq-equality/
38. KESQ, "Transgender Health & Wellness Center files complaint against county over discrimination" (Dec 9, 2025) — https://kesq.com/news/2025/12/09/transgender-health-wellness-center-files-complaint-against-county-over-discrimination/
39. KESQ, "'Empower and Employ' Transgender Resource Fair in Palm Springs today" (Mar 28, 2026) — https://kesq.com/news/2026/03/28/empower-and-employ-transgender-resource-fair-in-palm-springs-today/
40. The Palm Springs Post, "Weekend transgender employment event aims to break barriers and build community" — https://thepalmspringspost.com/weekend-transgender-employment-event-aims-to-break-barriers-and-build-community/
41. Gay Desert Guide, "Trans Pride 2026: Empowerment & Employment in Palm Springs" — https://gaydesertguide.com/trans-pride-2026-palm-springs-event-focuses-on-tgi-empowerment-and-employment/
42. The Outwords Archive, Thomi Clinton oral-history interview — https://theoutwordsarchive.org/interview/thomi-clinton/

---

# SECTION 1 — EXECUTIVE SUMMARY

**Who the organization appears to be.** The Transgender Health and Wellness Center (TH&WC, also written THWC/THAWC) is a trans-led 501(c)(3) nonprofit headquartered in Palm Springs, CA, describing itself as "the largest Trans-led organization" in Southern California (trans.health). It grew out of the Transgender Community Coalition (formed 2014) and was founded with roughly $10,000; it now reports 40+ staff across multiple locations on its website, ~61 employees per GuideStar/Cause IQ, and 2024 revenue of about $4.08M against $3.45M expenses (ProPublica; GuideStar; Cause IQ). It holds a California HCAI **Community Clinic** license (HCAI facility record) and an NPI as a Clinic/Center (NPI 1639024938), and it earned a 4/4-star Charity Navigator rating.

**What it serves and does.** It serves transgender, gender-nonconforming, and intersex (TGI) people — plus LGBTQ+ youth, families, and allies — across Riverside, San Bernardino, and San Diego counties (findhelp.org listings; trans.health/locations). Core services: medically necessary gender-affirming hair removal (laser and electrolysis, billable to insurance/Medi-Cal), free telehealth mental health care for adults and youth with no insurance required, HIV/AIDS education and linkage to care, housing assistance, employment support, legal name/gender-marker change assistance, food/clothing/hygiene emergency aid, support groups, and community events including the annual "Trans Pride: Empower and Employ" resource fair (trans.health; GuideStar; KESQ; LawHelpCA).

**Likely operational pain points.** **[INFERENCE]** A multi-county, multi-site, ~60-person hybrid organization (licensed clinic + social-services agency + community center + advocacy org) that grew from $10K to $4M in under a decade almost certainly runs on a patchwork of phone/email intake, spreadsheets, siloed clinical and case-management records, manual grant reporting, and staff heroics. Public evidence supports this: intake appears to be phone/email-based (contact pages list phone and info@trans.health; no client portal is visible), events run on Eventbrite (an external consumer platform), volunteers are recruited through third-party sites (TurnOut, Idealist), and the December 2025 loss/withdrawal of a county HUD contract worth $132,000 (KESQ) shows both funding volatility and the burden of contract compliance reporting.

**Why an all-in-one platform could help.** TH&WC's clients often need three to six services at once (hormones navigation + mental health + housing + legal + food). Today each has a different front door. A single privacy-first platform can (1) give clients one safe, discreet way to reach every program, (2) give staff one queue, one case record, and one referral tracker instead of parallel systems, and (3) generate the aggregated outcome data that state grants (e.g., CDPH TGI Fund) and private funders require — without exposing individual identities.

**Highest-value app concept.** "**Oasis**" (working name): a mobile-first, stealth-capable front door to TH&WC — request services, track your care journey, message your navigator, find verified resources, and RSVP to community events — backed by a staff console that unifies intake triage, case management, referrals, scheduling, and privacy-preserving grant reporting.

**Top 5 risks to avoid.**
1. **Outing users** through notifications, shared devices, subpoenas, or data breach — in a federal policy climate that is actively hostile (see the Dec 2025 county contract dispute, KESQ). Design for deniability, minimal data, and user-controlled visibility.
2. **Building a HIPAA problem instead of a HIPAA solution** — the org includes a licensed community clinic; anything touching clinical care must be treated as PHI with a compliant stack and BAAs.
3. **Staff overload from a second system** — if the platform doesn't *replace* spreadsheets/phone tag, it becomes one more inbox. MVP must reduce, not add, staff work.
4. **Overbuilding** — a 60-person nonprofit with volatile funding cannot maintain a sprawling custom system. Build the thinnest slice that moves the needle; buy where safe.
5. **Community mistrust** — one bad privacy incident or one misgendering flow destroys adoption in a tight-knit community. Co-design with TGI community members and publish the privacy model in plain language.

---

# SECTION 2 — PUBLIC-SOURCE ORGANIZATION PROFILE

## 2.1 Verified facts

**Identity and status**
- Official name: **Transgender Health and Wellness Center**; abbreviations in public use: **TH&WC** (own site), **THWC**, **THAWC** (Outwords Archive; ZoomInfo) (trans.health; theoutwordsarchive.org).
- Certified 501(c)(3) nonprofit; EIN **82-4659164** (trans.health; ProPublica; GuideStar).
- Self-described as "the largest Trans-led organization" operating across Southern California, employing "the most Transgender, Gender Non-Conforming and Intersex (TGI) people of any Southern California nonprofit" (trans.health/about-us).
- Origin: the Transgender Community Coalition (TCC) formed in 2014; TH&WC was founded with its help. Sources differ on founding year — the site narrative says founded 2018 with $10,000; GuideStar lists formation in 2019; the founder's bio pages reference 2015. **[UNKNOWN — exact incorporation vs. program-launch dates; confirm with org.]**
- Founder/CEO: **Thomi Clinton**, publicly listed on the org's own team page (trans.health/team/thomi-clinton) and covered by press (KESQ; Outwords Archive). Publicly reported: she founded TCC, has advised on national LGBTQ+ health and PREA policy, and received the HRC Community Impact Award in November 2025 (KESQ, Nov 8, 2025). One KESQ story styles her "CRO" while others say "CEO and founder" — title to confirm. **[UNKNOWN — current title/org chart.]**
- Regulatory footprint: California HCAI facility record with license type **Clinic**, category **Community Clinic** (hcai.ca.gov); **NPI 1639024938**, taxonomy Clinic/Center, listed in Oceanside, CA (npiprofile.com).
- Charity Navigator rating: **4/4 stars** (charitynavigator.org/ein/824659164).

**Scale and finances**
- Website: "more than 40 staff in all 5 locations" (trans.health/about-us). GuideStar/Cause IQ: **61 employees**. 40+ active volunteers (trans.health/volunteer).
- 2024 financials (most recent public filing summarized by ProPublica/GuideStar/Cause IQ): total revenue **$4,082,462**; total expenses **$3,447,232**; total assets **$1,987,488**. Form 990s available 2018–2024 (ProPublica).
- Founded "with only $10,000"; now "over a million-dollar budget" per the site narrative (trans.health/about-us) — the filings show it has in fact passed $4M.

**Locations and service area** (trans.health/locations; findhelp.org; Yelp business listing; gaydesertguide.com)
- Palm Springs: 340 S. Farrell Drive (suites A208 and A106 both appear in public listings), Palm Springs, CA 92262 — also the donation mailing address.
- Cathedral City: 35325 Date Palm Drive, Suite 143, Cathedral City, CA 92234; phone (760) 202-4308.
- Riverside: 6840 Indiana Ave, Suite 150, Riverside, CA 92506 (weekday hours listed on findhelp).
- San Diego: 3737 Moraga Ave, Suite A204, San Diego, CA 92117 (Yelp listing categorizes it under laser hair removal).
- An NPI record lists an Oceanside, CA clinic address (npiprofile.com). The site claims 5 locations; public listings surface 4–5 addresses. **[UNKNOWN — current authoritative list of open sites.]**
- Program service area on findhelp: residents of **Riverside, San Bernardino, and San Diego counties**.

**Mission and services** (trans.health home/about; GuideStar; findhelp; LawHelpCA)
- Stated scope: "a wide range of social services — including HIV/AIDS education, housing, employment, linkage to care, legal guidance, counseling, and other supportive services for the Transgender, Gender non-conforming, and Intersex (TGI) community" (trans.health/about-us).
- **Gender-affirming hair removal**: "medically necessary gender affirming permanent hair removal" via laser and electrolysis; many electrologists are themselves trans/gender-diverse; revenue from hair removal is reinvested in the community (trans.health/services/hair-removal-service; GuideStar). Context: Medi-Cal covers medically necessary hair removal with documented gender-dysphoria diagnosis and referral (Health Net provider library; Medi-Cal news).
- **Mental health**: free telehealth mental wellness program for LGBTQ+/TGI adults and youth; "completely free and does not require insurance" (GuideStar; trans.health).
- **Housing**: rental assistance, emergency housing support; emergency and transitional clothing for LGBTQ+ youth kicked out or in foster transitions (trans.health; Facebook group description; KESQ Oct 2024).
- **Legal**: name and gender-marker change assistance and guidance with legal documents (trans.health; LawHelpCA listing).
- **Basic needs**: emergency hygiene supplies, food (including pet food) (trans.health; Facebook group description).
- **Insurance navigation**, including offering to meet employers' HR departments to improve TGI-affirming coverage (trans.health/services/insurance-navigation).
- **Support groups**: online groups for trans/nonbinary people, allies, family, friends, partners (trans.health/resources/support-groups).
- **Grief counseling** appears among listed services on the San Diego business listing (Yelp).
- **Healing Rainbows**: a space opened October 2024 dedicated to connecting TGI and allied individuals with housing, mental health, and food assistance (KESQ, Oct 10, 2024).

**Events and outreach**
- Annual **Trans Pride "Empower and Employ"** resource/employment fair in Palm Springs: 2025 edition drew hundreds (KESQ, Mar 29, 2025); 2026 edition held March 28 at Demuth Community Center with resource booths, performances, food trucks, and a youth zone; free admission (trans.health event page; KESQ; Gay Desert Guide; Palm Springs Post).
- Active Eventbrite organizer account for events (Eventbrite).
- Weekly support groups and monthly social get-togethers (Gay Desert Guide directory).

**Funding and government relationships**
- Grantee of the California Department of Public Health's **TGI Wellness and Equity Fund** (established by AB 2218, 2020): one of five organizations sharing nearly $2.4M in clinical-services grants for gender-affirming health care (lachealthequity.substack.com; CDPH TGI Unit).
- Multi-year partnership with the **County of Riverside / Continuum of Care** (HUD-funded housing dollars). The most recent HUD-funded agreement ended; in December 2025 TH&WC filed a complaint with California's Civil Rights Department alleging the county inserted discriminatory contract language tied to a federal executive order barring reimbursement to groups "promoting gender ideology"; the org said it could not sign without risking **$132,000** in reimbursements (KESQ, Dec 9, 2025). The org posted a public "Housing Program Notice Regarding Federal Funding" acknowledging that some federally funded housing programs may be unavailable to organizations providing gender-affirming services (trans.health/notice).
- Recognition: honored alongside the City of Palm Springs by the Human Rights Campaign, Nov 2025 (KESQ).

**Communication channels**
- Website trans.health; email info@trans.health; phone (760) 202-4308 (Cathedral City listing); Instagram @transhealthandwellnesscenter; Facebook page(s) including a San Diego-specific page and a community Facebook group ("TransCC"); Eventbrite; online donation page plus mail-in checks; volunteer recruitment via its site, TurnOut, and Idealist.

## 2.2 Reasonable inferences **[INFERENCE]**

1. **Hybrid operating model**: TH&WC is simultaneously (a) a licensed community clinic (HCAI license, NPI) delivering billable services (hair removal; likely behavioral health), (b) a social-services/case-management agency (housing, employment, basic needs, linkage to care), (c) a community center (groups, events), and (d) an advocacy organization (civil-rights complaint, policy roles). Each mode has different data, compliance, and workflow needs — a central design challenge.
2. **Revenue mix is a braid of state grants, county contracts, service billing, and donations** — supported by the TGI Fund award, the county CoC history, Medi-Cal-billable hair removal, and active donation/volunteer pages. Federal-facing revenue is now unstable for political reasons (the December 2025 dispute), pushing the org toward state, private, and earned revenue — which raises the value of strong outcome data for fundraising.
3. **Intake is likely manual and phone/email-centric**: no client portal, online scheduling, or intake form is visible in any indexed page; contact pages emphasize phone and email. For a five-site, three-county organization, this implies duplicate data entry, missed calls, and waitlist opacity.
4. **Fragmented tooling**: Eventbrite for events, third-party volunteer boards, likely a separate EHR/billing tool for the clinic (a Salesforce-based navigator job ad pattern is common in this sector), and general-purpose office tools elsewhere. **[UNKNOWN — actual internal systems.]**
5. **Clients skew high-need and mobile-first**: services offered (emergency food, hygiene, clothing, rental assistance, foster-youth support) indicate many clients experience poverty, housing instability, or family rejection; smartphone-only internet access is the safe design assumption.
6. **Geography is a real barrier**: three counties spanning ~150 miles with sites in the Coachella Valley, Riverside, and San Diego; the org already leans on telehealth for mental health, implying demand for more remote-first service delivery.
7. **Staff include many community members** (the org highlights employing TGI people, and trans electrologists) — meaning staff themselves have heightened privacy stakes in any internal system.

## 2.3 Unknowns requiring stakeholder confirmation **[UNKNOWN]**

- Exact legal/corporate structure of clinic vs. nonprofit programs; HIPAA covered-entity status and current compliance posture.
- Current EHR/EMR, billing, case-management, CRM, donor, and reporting systems actually in use.
- Authoritative list of open locations, staffed programs, and current headcount by role.
- Whether the org serves minors directly in mental health (public materials say "adults and youth") and under what consent framework.
- Current funders and reporting requirements beyond CDPH TGI Fund and the ended county contract.
- Waitlist sizes, no-show rates, call volume, and where staff time actually goes.
- Board composition and technology appetite/budget.
- Languages needed (Spanish is a near-certain requirement in Riverside/San Bernardino/San Diego counties — **[INFERENCE]**).

---

# SECTION 3 — STAKEHOLDER MAP

## 3.1 External users

**1. Transgender and nonbinary adults seeking gender-affirming services (hair removal, HRT navigation, surgery navigation)**
- *Needs:* find out what TH&WC offers, whether it's free/covered, how long the wait is, and get started without repeating their story.
- *Pain points:* phone-only intake during work hours; insurance/Medi-Cal paperwork (documentation of medical necessity is required for hair removal — Health Net provider library); long distances between sites.
- *Safety concerns:* being outed by mail, voicemail, or visible apps; data falling into hostile hands amid federal policy shifts (KESQ Dec 2025 context).
- *Digital literacy:* broad range; assume smartphone-first, variable data plans.
- *Privacy concerns:* legal name vs. chosen name mismatches; insurance explanation-of-benefits exposure.
- *Desired outcomes:* start services quickly, track referrals, control what's shared.
- *Features that help:* discreet onboarding, chosen-name-first records, service request wizard, referral status tracker, document upload for medical-necessity letters.

**2. People seeking free mental health / peer support**
- *Needs:* low-friction request for the free telehealth program; group schedules.
- *Pain points:* stigma; not knowing eligibility ("free, no insurance required" is a differentiator worth surfacing — GuideStar).
- *Safety concerns:* therapy participation visible to family/household.
- *Features:* private group calendar, telehealth links, crisis-routing separate from therapy waitlist.

**3. LGBTQ+ youth and young adults (incl. foster youth, family-rejected youth)**
- *Needs:* clothing, hygiene, food, safe adults, peer groups, youth zone events (trans.health; KESQ).
- *Pain points:* no transportation, no payment cards, parental surveillance of devices.
- *Safety concerns:* highest outing risk; possible mandatory-reporting interactions.
- *Digital literacy:* high app fluency, low bureaucracy tolerance.
- *Features:* stealth mode, quick exit, no-login resource browsing, clear "what happens if I tell you X" disclosures.

**4. People needing housing, food, transportation, or crisis help**
- *Needs:* immediate, accurate, TGI-safe referrals; rental assistance applications (trans.health; KESQ Oct 2024).
- *Pain points:* federal housing funding instability at TH&WC itself (trans.health/notice); shelters that are unsafe for trans people.
- *Safety concerns:* DV/stalking; data that could reach abusers.
- *Features:* urgency triage on intake, verified emergency directory, offline-cached resource pages, no location tracking.

**5. People seeking legal name/gender-marker change**
- *Needs:* step-by-step California workflow, document checklists, court-fee waiver info, clinic letters (LawHelpCA listing).
- *Features:* guided checklist, document vault, appointment booking with the legal-navigation team.

**6. People seeking HIV/STI education and linkage to care**
- *Needs:* confidential education, testing referrals, care linkage (trans.health/about-us).
- *Safety concerns:* California HIV confidentiality law (Health & Safety Code §120980) elevates the sensitivity tier.
- *Features:* referral tracking with extra-restricted visibility; nothing HIV-related in notifications, ever.

**7. Families, partners, allies**
- *Needs:* support groups (explicitly welcomed on the support-groups page), education.
- *Features:* ally-facing group signup that never exposes the trans person's records.

**8. Community event participants**
- *Needs:* discover Trans Pride, workshops, socials; RSVP without Eventbrite account friction.
- *Features:* public event calendar (no login), private RSVP.

**9. Donors and volunteers**
- *Needs:* easy giving (site currently offers online donation + mailed checks), volunteer shifts (40+ volunteers; TurnOut/Idealist listings).
- *Features:* donation flow, campaign pages, shift signup, hour logging that feeds grant reports.

## 3.2 Internal users

**Intake/front-desk staff** — need one queue for calls/walk-ins/web requests; today likely juggle phone, email, paper. Features: unified intake queue, dedupe, triage flags, callback scheduling.

**Case managers / navigators** — need caseload views, referral tracking across housing/legal/medical, note-taking, follow-up reminders. Pain: multi-program clients live in multiple systems. Features: single client record with program-scoped visibility, task lists, warm-referral handoffs.

**Clinicians / care coordinators (clinic side: electrologists, behavioral health)** — need scheduling, medical-necessity documentation, consent forms; their records are PHI. Features: appointment management, document requests, EHR integration boundary (the platform should *reference*, not replicate, clinical charts — see Section 11).

**Mental health providers** — need referral intake, group rosters, telehealth links; strict confidentiality walls from other programs.

**Outreach workers / event staff** — need event check-in, resource fair logistics, attendance counts for reporting (hundreds at Trans Pride — KESQ).

**Program managers** — need utilization dashboards, waitlist visibility, staff workload views.

**Executive leadership** — needs cross-program metrics, funder-ready reports, evidence for advocacy (e.g., demonstrating demand when contracts are threatened — KESQ Dec 2025).

**Volunteers** — need onboarding, training tracking, shift signup; must see only what their role requires.

**Grant/finance staff** — need deduplicated service counts, demographics in funder formats (CDPH TGI Fund reporting), volunteer hours, event attendance — without hand-tallying spreadsheets.

**Communications staff** — need event publishing, resource updates, impact stories (with consent), channel management across Instagram/Facebook/site.

**Administrators** — need user/role management, audit review, data retention execution, incident response tooling.

---

# SECTION 4 — PROBLEM DIAGNOSIS

Severity scale: ▲ high / ● medium / ○ low. "Evidence" = public signal; reasoning marked [INF] = inference.

| # | Problem | Evidence / reasoning | Severity | Who's affected | Likely current workaround | App opportunity |
|---|---|---|---|---|---|---|
| 1 | **Fragmented front door** | Services span clinic, mental health, housing, legal, basic needs (trans.health); contact = phone/email only; no visible portal | ▲ | Clients, intake staff | Call (760) 202-4308 or email info@trans.health; walk in | One intake wizard routing to all programs |
| 2 | **Phone-hours barrier** | Weekday 10–5 office hours (findhelp); working/closeted clients can't call [INF] | ▲ | Clients | Voicemail, missed connections | 24/7 async service requests with callback preferences |
| 3 | **Repeat storytelling across programs** | Multi-service clientele (housing+MH+legal+clinic) [INF from service breadth] | ▲ | Clients, case managers | Re-intake per program | Single consented client record, program-scoped |
| 4 | **Referral black holes** | "Linkage to care" is a core service (trans.health); external referrals (surgery, HIV care, shelters) lack shared tracking [INF] | ▲ | Clients, navigators | Sticky notes, email threads | Referral objects with status, owner, follow-up dates |
| 5 | **Waitlist opacity** | Free-MH + hair-removal demand across 3 counties; no public wait info [INF]; Medi-Cal gender-care access is documented as hard statewide (California Healthline) | ● | Clients, managers | "Call back next month" | Waitlist position + honest expectations in-app |
| 6 | **Insurance/medical-necessity paperwork** | Hair removal requires diagnosis + referral documentation (Health Net provider library); org runs insurance navigation (trans.health) | ● | Clients, clinic staff | Fax/email/paper shuffling | Guided document checklist + secure upload |
| 7 | **Event ops on consumer platforms** | Eventbrite organizer page; Trans Pride draws hundreds (KESQ) | ● | Outreach, comms, attendees | Eventbrite + manual counts | Integrated events with private RSVP + attendance reports |
| 8 | **Volunteer coordination scattered** | Recruiting via TurnOut, Idealist, own page; 40+ volunteers | ● | Volunteer coordinators | Email + spreadsheets | Shift board + hour logs feeding grant reports |
| 9 | **Grant/contract reporting burden** | CDPH TGI Fund grantee; county contract compliance was disputed ("contractual requirements not fully met" per county, KESQ Dec 2025) | ▲ | Grant staff, leadership | Manual tallies from many tools | Auto-aggregated, de-identified outcome reports |
| 10 | **Funding volatility → need for demand evidence** | $132K county reimbursement standoff; public federal-funding notice (trans.health/notice) | ▲ | Leadership | Anecdote-driven advocacy | Trend dashboards: demand, waitlists, unmet need |
| 11 | **Safety for not-out users** | Client base includes youth in hostile homes, DV survivors [INF from clothing/foster/DV-adjacent services] | ▲ | Clients | Avoiding contact entirely | Stealth mode, quick exit, neutral notifications |
| 12 | **Geographic spread / transportation** | Sites 60–150 miles apart; service area = 3 counties (findhelp) | ● | Clients, staff | Long drives; telehealth for MH only | Telehealth-first flows, transport resource module |
| 13 | **Crisis triage mixed with routine intake** | Org serves people in acute housing/safety crises alongside cosmetic-adjacent bookings [INF] | ▲ | Intake staff, clients | Whoever answers the phone decides | Urgency triage at intake + crisis routing rails |
| 14 | **Continuity of care across sites/staff turnover** | 61 employees, 5 sites; nonprofit turnover is endemic [INF] | ● | Clients, managers | Institutional memory | Structured notes, tasks, handoff views |
| 15 | **Resource directory drift** | Org is itself listed in many directories; maintaining outbound referral lists (TGI-safe shelters, providers) is manual [INF] | ● | Navigators, clients | Google Docs / memory | Verified directory with review dates + suggestion queue |
| 16 | **Outcome tracking for care journeys** | TGI Fund funds clinical services; funders increasingly demand outcomes (CDPH RFA) | ● | Grant staff, leadership | Exit surveys, ad hoc | Consented outcome check-ins tied to service episodes |
| 17 | **Mobile-first access gap** | No app; site is informational [INF from public surface] | ● | Clients | Phone calls | PWA/mobile app as primary client surface |
| 18 | **Trust maintenance at scale** | Community trust is the org's core asset (trans-led identity is central to its brand — trans.health) | ▲ | Everyone | Personal relationships | Privacy-first design that *visibly* protects users |

---

# SECTION 5 — COMPETITIVE AND COMPARABLE LANDSCAPE

**LGBTQ+ center platforms (LA LGBT Center / Trans Wellness Center, mytranswellness.org).** The LA Trans Wellness Center consolidates multiple partner orgs' trans services under one roof and one website. *Does well:* single-front-door concept, clear service menus. *Fails trans users:* still largely brochureware — the "app" experience is calling numbers; no self-service tracking. *Don't copy:* LA-scale partner federation complexity. *TH&WC opportunity:* be the first mid-size trans-led org whose front door is genuinely transactional (request → track → complete), not informational.

**FQHC patient portals (Epic MyChart at big systems; eCW/athena at community clinics; e.g., DAP Health/Borrego in TH&WC's region).** *Do well:* appointments, secure messages, results — mature and HIPAA-hardened. *Fail trans users:* legal-name-first architecture (deadnaming in every header), clinical-only scope (no housing/legal/community), intimidating tone, and notification defaults that leak ("Your lab results from X Clinic"). *Don't copy:* forcing an EHR portal to be a community hub. *Opportunity:* a warm navigation layer *in front of* clinical systems, with chosen-name-everywhere and social services as first-class citizens.

**Nonprofit case-management tools (Apricot/Bonterra, CaseWorthy, Salesforce Nonprofit Cloud, Penelope).** *Do well:* configurable programs, funder reports, HMIS-style exports. *Fail trans users:* they are staff tools only — clients have no safe self-service surface; gender fields are often binary or clumsy; per-seat pricing punishes growth. *Don't copy:* their client-facing afterthought portals. *Opportunity:* pair a humane client app with a right-sized staff console; consider *integrating* with such a tool rather than rebuilding reporting depth (see build-vs-buy, Section 20).

**Community resource apps (findhelp.org/Aunt Bertha, One Degree).** TH&WC is already listed on findhelp. *Do well:* huge indexed directories, closed-loop referral plumbing. *Fail trans users:* listings aren't vetted for trans safety — a "shelter" result can be actively dangerous; generic taxonomies miss gender-affirming specifics. *Don't copy:* breadth-over-safety indexing. *Opportunity:* a *curated, staff-verified, trans-competence-rated* directory (smaller but trustworthy), optionally fed by findhelp's API.

**Appointment/intake SaaS (Calendly, Acuity, SimplePractice, Jotform).** *Do well:* frictionless booking/forms. *Fail trans users:* consumer-grade privacy defaults, name handling, and no triage — a crisis and a laser consult look identical. *Don't copy:* auto-confirm emails with service names in subject lines. *Opportunity:* request-based (not self-book) scheduling with staff approval and neutral messaging.

**Donor/volunteer platforms (Givebutter, Bloomerang, Galaxy Digital, SignUpGenius).** *Do well:* payments, CRM, shift logistics cheaply. *Fail this context:* donor CRMs must never touch client data; combined tools tempt catastrophic joins. *Don't copy:* unified "constituent" records across donors and clients. *Opportunity:* keep donor/volunteer modules architecturally separated from client data; integrate a processor rather than building payments.

**Gender-affirming care platforms (Plume, FOLX, QueerDoc).** *Do well:* discreet, chosen-name-first UX; telehealth-native; excellent tone — the best UX benchmark for this project. *Fail this context:* subscription-priced, virtual-only, medical-only; they don't do housing, legal aid, food, or community, and they're competitors for HRT rather than partners for wraparound care. *Don't copy:* subscription paywalls. *Opportunity:* Plume-quality UX applied to a free, community-rooted, whole-person service model — which none of the venture platforms address.

**Crisis/safety tools (Trans Lifeline, THRIVE Lifeline, 988).** *Do well:* clear crisis boundaries, peer-run credibility. *Lesson:* the app must route crises out to competent services and never imply it *is* a crisis line — with honest copy about response times.

**Net opportunity.** No existing product combines: (1) trans-led community trust, (2) clinical + social + legal + community scope, (3) client self-service with stealth-grade privacy, and (4) nonprofit-grade reporting. That intersection is TH&WC's to own — and is only credible because TH&WC already operates all four legs organizationally.

---

# SECTION 6 — PRODUCT VISION

**Working name:** **Oasis** (by TH&WC) — a desert-region nod (Coachella Valley home base) that reads as a generic wellness word to a shoulder-surfer. Alternate neutral install label for stealth contexts: "Oasis Wellness."

**Positioning statement:** Oasis is the safe front door to the Transgender Health and Wellness Center — one private place to ask for help, follow your care, find trusted resources, and join community across Southern California.

**Core product promise:** *"Ask once. Stay in control. We'll walk with you."* — one intake reaches every program; the client controls what is shared and how they're contacted; staff follow through visibly.

**Primary user experience (client).** A mobile-first app/PWA where a client can: browse services and verified resources without an account; create a discreet account with a chosen name; complete one adaptive intake; request any service (hair removal consult, free therapy, housing help, legal navigation, HIV linkage); see honest status ("You're #14 on the electrolysis waitlist; average wait ~6 weeks"); message their navigator; get consent-controlled, neutral-text reminders; RSVP to groups and events; and vanish quickly (quick-exit, stealth label, remote sign-out).

**Internal staff experience.** A web console where intake staff work one triaged queue across phone/walk-in/web; navigators manage caseloads, referrals, and tasks on a single client timeline; clinic staff handle appointment requests and document checklists; event/volunteer coordinators run logistics; and every screen enforces program-level need-to-know.

**Community impact thesis.** Every hour not spent on phone tag and re-keyed spreadsheets is an hour of direct service. Every client who can ask for help at 2 a.m. without saying their deadname out loud on a hallway phone call is a client who asks sooner. Every funder report generated from real, de-identified service data strengthens the case for the org's survival in a hostile funding climate (trans.health/notice; KESQ Dec 2025).

**Why one integrated platform, not disconnected tools.** (1) The *client* is integrated — the same person needs therapy, electrolysis, housing, and a court form; only a shared (consented) record prevents re-traumatizing repetition. (2) The *reporting* is integrated — funders ask "how many people did you serve, with what outcomes," which is unanswerable across five disconnected SaaS silos without manual dedup. (3) The *safety model* must be integrated — privacy guarantees are only as strong as the weakest tool in the chain; one platform means one enforced policy for names, notifications, and access. (4) The *organization* is small — five admin panels cost more in training and licenses than one coherent system. (Deliberate exceptions: payments, EHR/clinical charts, and payroll stay in specialized systems — see Sections 15–16.)

---

# SECTION 7 — CORE MODULES

### Module 1 — Safe Welcome / Stealth Mode
- Neutral app identity option: installable PWA lets users choose the home-screen label/icon ("Oasis Wellness," plain compass icon); native builds ship a discreet default.
- **Quick exit**: persistent button + shake gesture → swaps to a weather page and clears back-stack; does not log the user out unless they choose "exit + lock."
- Privacy-first onboarding: browse everything public (services, events, resources) with **no account**; account creation asks only email-or-phone + chosen name; explicit plain-language explanation of what is stored and who can see it.
- Chosen name and pronouns are the primary display fields everywhere; legal name is a separate, purpose-gated field collected **only** when a specific service requires it (insurance billing, court forms), with an inline "why we ask" note.
- Shared-device safety: biometric/PIN app lock, no content in app-switcher preview, session timeout, remote sign-out of all devices, warning banner when notifications are enabled on a device without a lock screen.
- Low-data mode: text-first screens, cached resource directory for offline use, no autoplay media.

### Module 2 — Client Intake and Eligibility
- One adaptive intake: identity basics (chosen-name-first), county of residence (service-area check for Riverside/San Bernardino/San Diego per findhelp listing), service interests (multi-select across all programs), access needs (language, disability accommodations), contact-safety preferences ("OK to leave voicemail? OK to text? Safe hours?"), referral source.
- **Urgency triage**: "Do you need help today?" branch → crisis resources + priority queue flag (see Module 4 boundaries).
- Granular consent capture at intake: per-program data sharing, contact channels, reminder types — stored as revocable consent records.
- Document upload (ID, referral letters, insurance card) deferred until a service actually needs it; never required to start.
- Insurance/payment info collected **only** for clinic services that bill (hair removal is Medi-Cal-billable with documentation — Health Net provider library); free programs (mental wellness is "completely free, no insurance required" — GuideStar) skip it entirely.
- Data minimization rule enforced in the form engine: every field maps to a documented purpose; demographic questions beyond service need are optional and labeled "helps us fund these services — never required."

### Module 3 — Gender-Affirming Care Navigation
- Care pathway overviews written for TH&WC's actual offerings: hair-removal course of treatment (laser vs. electrolysis, medical-necessity documentation steps), HRT *navigation* (TH&WC publicly does linkage/navigation, not visible prescribing — **[UNKNOWN: confirm]** — so the pathway is "we connect you to affirming prescribers + insurance navigation"), surgery-referral navigation, and letter support.
- Checklist engine per pathway: e.g., "Electrolysis via Medi-Cal: ① gender-dysphoria diagnosis letter ② referring-provider form ③ consult booked" with document slots and staff verification.
- Provider referral tracking: which external provider, date sent, status, follow-up owner.
- Educational library: appointment prep guides, what-to-expect articles, insurance navigation explainers (mirroring trans.health/services/insurance-navigation).
- Optional reminders (labs, follow-ups, hair-removal sessions) — **opt-in only**, neutral wording ("You have an upcoming appointment"), per-reminder revocable.

### Module 4 — Mental Health / Peer Support Navigation
- Request the free telehealth mental wellness program (adults and youth — GuideStar) via a short, warm form; honest wait expectations.
- Support-group calendar (online groups for trans/nonbinary folks, allies, families, partners — trans.health/resources/support-groups) with private RSVP and join links delivered in-app, not by email subject line.
- Peer-support signups and monthly social listings (Gay Desert Guide notes weekly groups/monthly socials).
- **Crisis boundary rails**: every mental-health surface carries a persistent, calm banner: "This app is not monitored 24/7. If you're in danger or crisis right now:" → 988 (with LGBTQ+-youth option), Trans Lifeline, THRIVE, local county crisis lines, 911 guidance with honest caveats. Crisis routing works logged-out and offline-cached.
- Safety-planning template (self-guided, stored client-side/encrypted, shareable with a therapist only by explicit action).

### Module 5 — Legal and Social Services Navigation
- California name/gender-marker change workflow: guided checklist (petition, fee waiver, courts by county, DMV, Social Security, passport realities under current federal policy — flagged as "changes often; verified [date]"), document vault, request help from TH&WC's legal-guidance team (LawHelpCA listing confirms this service).
- Housing: request rental assistance / emergency housing support (KESQ Oct 2024; trans.health), with transparent notes where federal funding constraints affect availability (mirroring the org's own public notice — trans.health/notice).
- Food & basic needs: request hygiene kits, food (including pet food — Facebook group description), clothing closet (emergency/transitional clothing for youth — trans.health).
- Employment: job-readiness resources and a bridge to the annual Empower and Employ fair pipeline (KESQ Mar 2026).
- Benefits navigation (Medi-Cal enrollment help via insurance-navigation program).
- Immigration-sensitive referrals: curated external partners only; **no immigration-status field anywhere in the data model**.
- DV/safety resources: discreet placement, quick-exit aware, includes trans-competent shelter/DV orgs vetted by staff.

### Module 6 — Appointment and Service Scheduling
- Request-first model (not open self-booking): client picks service + site (Palm Springs, Cathedral City, Riverside, San Diego — trans.health/locations) or telehealth + general availability; staff confirm → client accepts. Prevents triage bypass and no-show-prone auto-booking.
- Waitlist objects with position/ETA honesty; automatic offer of cancellations ("A Thursday slot opened — want it?").
- Reminders: opt-in, channel-per-client (push/SMS/email), **neutral text by default** ("Reminder: appointment Thu 2pm" — no service name, no org name in SMS unless the client opts into explicit mode).
- Reschedule/cancel in two taps; reasons optional.
- Telehealth: join links surfaced in-app at T-15min; staff-side links to the org's video tool (integration, not a custom video build).
- Staff calendar sync (Google/Microsoft) one-way from platform → staff calendar with privacy-safe titles ("Client session — see console").

### Module 7 — Secure Messaging
- Client ↔ assigned staff threads, program-scoped (a housing thread isn't visible to clinic staff without consent).
- Thread assignment, transfer, and escalation tags (urgent / safety / supervisor review).
- Response-time expectation set in-thread ("We reply within 2 business days; this inbox is not for emergencies" + crisis links).
- Notifications: "You have a new message" only; content never in push/SMS/email.
- Staff-side: canned snippets, internal notes invisible to client (clearly marked), full audit log of reads/writes.
- Attachments route through the document vault with virus scanning.

### Module 8 — Resource Directory
- Curated, **staff-verified** listings: trans-competent medical providers, therapists, shelters, food, transportation, legal aid, mutual aid, HIV/STI testing — each with "verified by TH&WC staff on [date]" and trans-safety notes.
- Emergency subset cached offline and available without login.
- Community suggestion form → staff review queue; stale-listing alerts (re-verify every N months).
- Filters: county (Riverside/San Bernardino/San Diego), telehealth, cost, language, wheelchair access.
- Optional integration: pull candidate listings from findhelp.org API into the *review queue* (never auto-published) — TH&WC already exists in that ecosystem.

### Module 9 — Events and Community
- Public calendar (no login): Trans Pride "Empower and Employ," workshops, support groups, socials (Eventbrite history; Gay Desert Guide).
- Private RSVP (attendance never publicly visible); household/guest counts; accessibility requests.
- Volunteer shifts attached to events; QR/code check-in for attendance counts (replacing Eventbrite scans) feeding aggregate reports ("hundreds attended" becomes an auditable number for funders — cf. KESQ Mar 2025).
- Post-event micro-surveys (2 questions, optional, anonymous by default).
- Youth-zone events flagged with appropriate safeguards. **[UNKNOWN: org's minor-participation policies.]**

### Module 10 — Volunteer and Donor Portal
- Volunteer onboarding: application, orientation/training tracking, agreement e-sign, background-check status flag if org policy requires **[UNKNOWN]**; shift board with self-signup and hour logging (auto-summed for grant reports).
- Donor flows: one-time/recurring gifts via embedded processor (Stripe/Givebutter — integration, not custom payments), campaign pages per program ("Fund a hygiene kit," "Sponsor electrolysis sessions"), in-kind needs list (clothing closet, pantry items — matching real programs), employer-match prompts, impact updates fed by *aggregate* platform stats only.
- **Hard wall**: donor/volunteer identities live in a separate data domain from client records; a person may exist in both, unlinked, by design.

### Module 11 — Staff Dashboard
- Intake queue with triage lanes (crisis-flagged / standard / info-only), source tags (web/phone/walk-in/event), dedupe suggestions.
- Case view: client timeline across consented programs, notes (structured + free-text), tasks with due dates, referral tracker, document checklist status.
- Appointment request board per site/service; waitlist management.
- Resource-directory admin; event and volunteer admin.
- Program metrics per manager: open cases, time-to-first-contact, waitlist depth, follow-up overdue counts.
- Exportable, de-identified grant reports (counts by service, county, month; demographics only in funder-required aggregate bands).
- Role-based access control throughout (see Section 11 permission model).

### Module 12 — Leadership / Reporting Dashboard
- Cross-program utilization, demand trends, waitlist trends, unmet-demand log (requests the org couldn't serve — potent advocacy evidence given the county funding fight, KESQ Dec 2025).
- Event attendance, volunteer hours, donation totals (from the walled donor domain, aggregate only).
- Outcome metrics (consented check-ins: housing stability, care-goal completion, wellbeing pulse).
- Demographic reporting with privacy safeguards: k-anonymity floor (suppress any cell < 10), no client-level export from this dashboard, no geographic granularity finer than county/city aggregates.
- Funder-report templates (CDPH TGI Fund style; foundation formats) with one-click period exports.

---

# SECTION 8 — USER JOURNEYS

**Journey 1 — A trans woman seeking hormone-care navigation.**
*Entry:* Googles "trans HRT help Palm Springs" → trans.health → "Get the app / start online." *State:* hopeful, wary, tired of explaining herself. *Steps:* browses HRT-navigation pathway logged-out → creates account with chosen name "Maya" → intake selects HRT navigation + insurance help → sees "a navigator will reach out within X business days; you choose how" → picks "text, afternoons only, no voicemail" → navigator messages in-app, books telehealth consult → referral to affirming prescriber tracked with statuses; insurance-navigation checklist runs alongside. *Safety:* legal name requested only when insurance step starts, with explanation; SMS says only "You have a new message." *Staff-side:* request lands in intake queue tagged "GAC-navigation," auto-assigned by county; navigator uses referral tracker + snippets. *Success:* first prescriber appointment booked; Maya rates the handoff 5/5 in a one-tap pulse. *Failure modes:* no navigator capacity (mitigate: honest waitlist + resource alternatives); referral partner unresponsive (mitigate: follow-up task auto-escalates at 14 days).

**Journey 2 — A nonbinary young adult, privacy-anxious, seeking support.**
*Entry:* Instagram post (@transhealthandwellnesscenter) about a youth group → link. *State:* curious, scared of being outed at home. *Steps:* opens PWA in browser incognito → browses groups logged-out → reads the plain-language privacy page ("what we store, what we never do") → installs PWA with neutral "Oasis Wellness" label → account with chosen name only, no phone → RSVPs to online group; enables app PIN; notifications off. *Safety:* quick-exit rehearsed in onboarding; no email confirmations by default; group join link appears in-app only. *Staff-side:* facilitator sees RSVP count and chosen names only. *Success:* attends group; later self-refers to free therapy from inside the app. *Failure:* parent inspects phone (mitigate: neutral label, PIN, no lock-screen content); user under 18 (mitigate: youth flow with minor-consent rules — Section 11.4 — validated with counsel first).

**Journey 3 — A client needing legal name/gender-marker help.**
*Entry:* returning client taps "Legal" tile. *State:* determined, overwhelmed by forms. *Steps:* CA name-change checklist opens → answers county (Riverside) → checklist localizes (Riverside Superior Court, fee-waiver option) → uploads draft petition to vault → requests document-review appointment with legal-navigation staff (LawHelpCA-listed service) → reminder for court date (opt-in, neutral text). *Safety:* legal name necessarily present here — screen marked "sensitive view," excluded from app-switcher previews; vault docs encrypted, client-deletable. *Staff-side:* legal navigator sees only legal-program record + shared docs; marks steps verified. *Success:* granted order; app offers "update your records everywhere" checklist (DMV/SSA/passport caveats). *Failure:* federal document rules shift (mitigate:每 listing carries verified-date; staff bulk-update alerts).

**Journey 4 — A person in crisis / unstable housing needing urgent resources.**
*Entry:* 11pm, friend's phone, no account. *State:* acute stress. *Steps:* opens site/app → persistent "Need help now?" → logged-out crisis page: 988/Trans Lifeline/county crisis + tonight's shelter options from the **verified** directory (trans-safety-noted) + "request TH&WC housing help" one-screen form (name-or-alias, callback method, safe hours). *Safety:* no location permission asked; page cached offline; no account required; form warns "this queue is checked during business hours" so no one mistakes it for rescue. *Staff-side:* morning intake queue shows crisis-flagged request on top; staffer calls per stated safe hours; case opens if consented. *Success:* warm connection to shelter that won't misgender them; follow-up housing case. *Failure:* stale shelter info (mitigate: re-verification SLAs); after-hours emergencies (mitigate: unmissable crisis-line routing, never buried).

**Journey 5 — A returning client managing appointments and referrals.**
*Entry:* push: "You have an upcoming appointment." *State:* busy, juggling. *Steps:* opens app → home shows next electrolysis session, therapy-group RSVP, surgery-referral status ("packet sent to Dr. X 6/12; follow-up 7/10") → reschedules Friday session to Tuesday from offered slots → messages navigator about the referral. *Staff-side:* reschedule auto-updates site calendar; message lands in assigned thread. *Success:* zero phone calls needed. *Failure:* notification fatigue (mitigate: digest mode); stale referral status (mitigate: overdue-follow-up escalation to supervisor view).

**Journey 6 — Intake staffer processing new requests.**
*Entry:* 9am console login (SSO + MFA). *State:* high volume, interruption-rich. *Steps:* queue shows 14 new: 1 crisis-flagged (handled first per protocol), 6 service requests, 4 phone-message logs, 3 event questions → dedupe prompt merges a repeat requester (consented match) → assigns by program + county → sends templated first-contact messages honoring each client's channel preferences. *Safety:* staffer sees only intake-tier data; no clinical or housing case detail. *Success:* median time-to-first-contact drops from days (phone tag) to hours; nothing lost on voicemail. *Failure:* queue swamps staffing (mitigate: workload dashboards for managers; auto-acknowledgment sets expectations honestly).

**Journey 7 — Case manager coordinating referrals.**
*Entry:* caseload view, Monday planning. *State:* 40 cases, finite hours. *Steps:* dashboard sorts by overdue follow-ups → client J needs housing + therapy + name-change: creates three referral objects (internal therapy waitlist; external shelter partner; internal legal) → warm-handoff note to legal navigator (consent verified in-line) → logs county-funded service units with two taps (feeds grant report). *Safety:* sees only assigned/consented cases; every access logged. *Success:* nothing slips; quarterly report compiles itself. *Failure:* consent gaps block handoff (mitigate: in-flow consent request to client via app); partner org has no system (mitigate: referral tracks "sent via phone/email" manually).

**Journey 8 — Volunteer signing up for a shift.**
*Entry:* saw TurnOut listing or Instagram call → volunteer portal. *State:* eager, time-limited. *Steps:* application → orientation video + quiz → e-signs confidentiality agreement → browses shifts (Trans Pride setup, pantry packing, front-desk greeting) → signs up, gets calendar file → QR check-in on the day; hours auto-logged. *Safety:* volunteers get zero client-data access; event-day tools show first names/pronouns only where operationally needed. *Staff-side:* coordinator sees roster, gaps, hour totals. *Success:* volunteer hours feed the leadership dashboard and grant narratives. *Failure:* no-shows (mitigate: reminders + easy drop); over-eager volunteers requesting client access (mitigate: role model simply has no such grant).

**Journey 9 — A donor supporting a specific program.**
*Entry:* year-end Instagram campaign → campaign page. *State:* motivated by mission, wants specificity. *Steps:* "Fund gender-affirming care" page shows aggregate impact ("X hair-removal sessions provided in 2026") → gives $50/mo via processor → receipt + welcome email → quarterly impact digest (aggregates only). *Safety:* donor domain fully walled from client data; donor may themselves be a client — systems never link them. *Staff-side:* development staff see donor CRM records, campaign totals. *Success:* recurring revenue diversifies away from volatile government contracts (directly relevant post-Dec-2025 — KESQ). *Failure:* impact claims outpace data (mitigate: dashboard-sourced numbers only); processor outage (mitigate: hosted checkout fallback).

**Journey 10 — Executive director preparing grant/impact reporting.**
*Entry:* CDPH TGI Fund quarterly report due; board meeting Thursday. *State:* time-pressed, accuracy-critical. *Steps:* leadership dashboard → selects period + funder template → auto-compiled: unduplicated clients served by program/county, service units, waitlist depth, event attendance (Trans Pride check-ins), volunteer hours, outcome pulses — all k-anonymized → exports PDF/CSV → separately pulls "unmet demand" trend for the advocacy deck in the county dispute. *Safety:* no row-level client data ever leaves; export logged. *Success:* reporting shrinks from days of spreadsheet forensics to an hour of review. *Failure:* funder demands a field the platform doesn't capture (mitigate: Phase-0 mapping of every current funder's fields before schema freeze).

---

# SECTION 9 — INFORMATION ARCHITECTURE

## 9.1 Navigation map (client app)

```
Logged-out (public)
├── Home: "How can we help?" + Need Help Now (persistent)
├── Services (hair removal • mental wellness • housing • legal • HIV/STI • basic needs • insurance nav)
├── Events & Groups (public calendar)
├── Resources (verified directory; emergency subset offline)
├── About / Locations (4–5 sites + telehealth) / Contact
├── Donate / Volunteer (→ walled portal)
└── Privacy, in plain language

Logged-in client (tab bar)
├── Home (next steps, statuses, unread)
├── My Care (requests • waitlists • appointments • referrals • checklists • documents)
├── Messages
├── Community (events, groups, RSVPs)
└── More (profile & pronouns • consents • notification & safety settings • quick-exit setup • sign out everywhere)
```

## 9.2 Staff portal flow

```
SSO+MFA → Role home
├── Intake: queue → triage → dedupe → assign
├── Cases: caseload → client timeline → notes/tasks/referrals/docs
├── Scheduling: request board → confirm/waitlist → site calendars
├── Messaging: assigned threads → escalations
├── Directory admin: listings → verification queue → suggestions
├── Events/Volunteers: calendar → rosters → check-in → hours
└── Program metrics (manager scope)
```

## 9.3 Admin and leadership flows

```
Admin: users & roles → permission grants → audit log search → retention jobs → incident tools → integration keys
Leadership: cross-program dashboard → funder report builder → trend explorer → export (logged, aggregate-only)
```

## 9.4 Donor/volunteer flow (separate domain)

```
Public campaign/shift pages → account (donor/volunteer identity only)
→ give / sign up / log hours → receipts, impact digests
(no path exists from this domain to client records)
```

## 9.5 Data object map (relationships)

```
User(auth) 1—1 ClientProfile —— ConsentRecord(s)
ClientProfile 1—n ServiceRequest → (CaseAssignment → StaffUser)
ServiceRequest 1—n Referral / Appointment / StaffTask
ClientProfile 1—n MessageThread(program-scoped) 1—n Message
ClientProfile 1—n Document(vault) ; 1—n OutcomeMetric(consented)
Event 1—n RSVP (→ ClientProfile OR anonymous contact)
Event 1—n VolunteerShift → VolunteerProfile(separate domain) 1—n HourLog
DonorProfile(separate domain) 1—n Donation → Campaign
Resource(directory) —n— ResourceVerification(StaffUser, date)
Everything → AuditLog (append-only)
```

## 9.6 Permission model (summary; detail in §11)

Roles: `client`, `volunteer`, `donor-staff`, `intake`, `navigator`, `clinic-staff`, `mh-provider`, `outreach`, `program-manager`, `grants`, `comms`, `exec`, `admin`. Axes: **role × program × site × relationship** (assigned vs. unassigned). Default deny; client consent is a hard gate layered on top of role rights; break-glass access exists for safety emergencies and is loudly audited.

---

# SECTION 10 — DATA MODEL

Design rules first: (1) **collect nothing without a mapped purpose**; (2) chosen name is the display name everywhere, legal name is a nullable, purpose-gated field; (3) sensitivity tiers — T0 public, T1 contact, T2 service, T3 sensitive (health/HIV/DV/legal), with T3 encrypted at field level; (4) every table row carries created/updated/actor for audit; (5) client-initiated export and deletion are first-class operations.

| Entity | Purpose | Key fields | Sensitive fields (tier) | Retention concerns | Access roles | Deletion/export |
|---|---|---|---|---|---|---|
| **User** | Authentication only | id, contact handle, auth factors, status | contact handle (T1) | Keep minimal; purge failed signups 30d | self, admin | Delete on request → cascades per policy |
| **ClientProfile** | Person receiving services | chosen name, pronouns, county, language, access needs, contact prefs, safe-contact rules | legal name (T3, gated), DOB (T2), demographics (T3, optional) | Demographics only aggregate after case closure; profile archived N yrs per program rules **[legal review]** | self, assigned staff, intake (subset) | Full export (JSON/PDF) to client; deletion honored except where law requires retention (explained in-app) |
| **ConsentRecord** | Provable, revocable permissions | scope (program/data/channel), granted/revoked timestamps, version of consent text | — (T2) | Never delete while underlying data exists; tombstone after | self, assigned staff, admin | Export yes; delete only with parent data |
| **IntakeForm** | Entry snapshot | responses, source, urgency flag, referral source | health/housing answers (T3) | Snapshot immutable; archive with case | intake, assigned staff | Export yes |
| **ServiceRequest** | Unit of "help me with X" | program, status, priority, site, timestamps | program itself can be sensitive (HIV linkage = T3) | Drives unduplicated-count reporting; keep aggregate stats after purge | assigned staff, managers (counts) | Export yes; delete → keep de-identified stat row |
| **Appointment** | Scheduled service | service, site/telehealth, time, status, staff | service type (T2/T3) | Purge details after N yrs; keep counts | client(self), clinic/assigned staff | Export yes |
| **CaseNote** | Continuity of care | author, body (structured + free), visibility scope | body (T3) | Clinical notes may fall under medical-record retention (CA: 7+ yrs) **[legal review]**; social notes shorter | author, assigned team, supervisor | Client may request copy; deletion restricted by law — say so plainly |
| **Referral** | Track handoffs | target (internal/external resource), status, dates, owner, outcome | target type may reveal condition (T3) | Outcome field feeds funder closed-loop stats | assigned staff | Export yes |
| **Resource** | Directory listing | org, services, counties, cost, languages, trans-safety notes, verified-on, verifier | — (T0) | Stale = dangerous; re-verify SLA field | public read; directory-admin write | n/a |
| **Event** | Community calendar | title, venue, time, capacity, public flag, youth flag | — (T0) | Keep for attendance history | public read; outreach write | n/a |
| **RSVP** | Attendance | event, attendee ref or anon contact, guests, access needs, checked-in | linkage of person↔event (T2; youth events T3) | Purge person-linked RSVPs 90d post-event; keep counts | outreach (roster), client(self) | Export/delete yes |
| **VolunteerProfile** | Volunteer ops | name, contact, trainings, agreements, background-check status flag | check status (T2) | Keep hour logs (grant audits); purge inactive profiles 2y | volunteer(self), coordinator | Export/delete yes (hours anonymize) |
| **Donation** | Revenue | donor ref, amount, campaign, recurrence, receipt | donor identity (T1, walled domain) | Financial retention rules (7y) | development staff, finance | Donor export yes |
| **StaffTask** | Follow-through | case ref, due, owner, type, status | via case ref (T2) | Purge with case | assigned staff, manager | n/a |
| **MessageThread / Message** | Secure comms | participants, program scope, body, read receipts | body (T3) | Client-visible retention policy (e.g., 3y); no silent deletion | participants, supervisor (logged) | Client export yes |
| **Document** | Vault | owner, type, file ref (encrypted), linked request | contents (T3) | Client-deletable unless attached to legal/billing record (flagged) | owner, explicitly granted staff | Export/delete yes |
| **OutcomeMetric** | Impact evidence | case ref, measure, value, consented flag, period | health/housing status (T3) | Immediately also stored de-identified; identified copy purged on case closure + N | assigned staff; aggregates to leadership | Aggregate survives deletion |
| **AuditLog** | Accountability | actor, action, object, timestamp, reason(break-glass) | reveals who-accessed-whom (T3 for insiders) | Append-only, tamper-evident, 6+ yrs **[legal review]** | admin, compliance; client can request access-history summary | Never deleted early |

---

# SECTION 11 — PRIVACY, SECURITY, AND COMPLIANCE

## 11.1 Regulatory posture (with explicit assumptions)

- **HIPAA**: TH&WC holds a Community Clinic license (HCAI) and an NPI, and hair removal is billed as medically necessary care (Medi-Cal documentation requirements — Health Net provider library). **Assumption: at least part of the organization is a HIPAA covered entity conducting standard transactions.** Therefore: any platform component touching clinical scheduling, clinical documents, or health-related messaging must run on a HIPAA-eligible stack with signed **BAAs** (hosting, SMS/email vendors, video, storage). **Requires legal confirmation** of which programs sit inside vs. outside the covered entity (a hybrid-entity designation may be appropriate).
- **California CMIA** (Confidentiality of Medical Information Act): applies to medical information regardless of HIPAA edges; stricter in places. **[Legal review required.]**
- **California HIV confidentiality** (Health & Safety Code §120980 et seq.): HIV-related data gets the platform's most restricted tier; never in notifications, exports default-exclude it.
- **CCPA/CPRA**: nonprofits are generally exempt, but design to CPRA norms anyway (access, deletion, purpose limitation) — it's the right trust posture and future-proofs contracts. **[INFERENCE/assumption.]**
- **42 CFR Part 2**: only if TH&WC operates a federally-assisted SUD program — **[UNKNOWN; confirm].**
- **Minors**: public materials say mental wellness serves "adults and youth" (GuideStar). California permits minors 12+ to consent to outpatient mental health in defined circumstances; parental-access rules to minors' records are nuanced. **The youth flow must not ship until counsel signs off** on consent, parental access, and mandatory-reporting handling.
- **Mandatory reporting**: staff are likely mandated reporters (clinic/youth services). The app must disclose this honestly *before* a young person discloses ("If you tell us about abuse, here's what we're required to do").
- **FTC Health Breach Notification Rule / state breach laws**: apply to any non-HIPAA health data; incident-response plan must cover both regimes.

## 11.2 Threat model highlights (beyond generic web security)

1. **Household adversary** (parent, partner, abuser with device access) → stealth label, PIN lock, neutral notifications, no email trails by default, quick exit, remote sign-out.
2. **Shoulder surfer / shared device** → no names on lock screens, app-switcher blur, short sessions on unregistered devices.
3. **Hostile legal/political environment** (subpoenas, funder audits weaponized; cf. the county's "gender ideology" contract language — KESQ Dec 2025) → data minimization is the *primary* defense: don't store what you'd dread producing; document retention schedules and follow them; segregate advocacy/comms data from client data; counsel-reviewed subpoena-response runbook.
4. **Insider misuse** (small community; staff/clients overlap socially) → need-to-know scoping, access logging visible to compliance, client-facing "who accessed my record" summaries, break-glass with mandatory reason + after-action review.
5. **Breach → mass outing** → field-level encryption for T3, no analytics SDKs with third-party data sharing, aggressive purge jobs, tested incident-response with community-appropriate notification templates.
6. **Malicious signups / harassment** (fake RSVPs, hostile actors probing events) → private-by-default RSVP lists, venue details for sensitive gatherings released only to confirmed registrants, rate limiting, staff moderation queues.

## 11.3 Security architecture requirements

- Encryption in transit (TLS 1.2+) and at rest; **field-level envelope encryption** for T3 fields (legal name, HIV-adjacent data, DV notes, message bodies, documents).
- AuthN: passwordless email/SMS magic links *optional but discouraged for hostile-household users*; prefer passkeys + app PIN; staff SSO (Google/Microsoft) + enforced MFA.
- AuthZ: policy-based access control implementing role × program × site × assignment × consent; default deny; server-side enforcement only.
- Append-only audit log (hash-chained or WORM storage) covering reads of T3 data, exports, permission changes, break-glass.
- Data minimization gates in code review: new fields require a documented purpose + tier + retention entry.
- Secure notification service: template registry where every template is classified "neutral-safe" before it can be sent to a channel.
- Backups encrypted, tested restores quarterly; DR runbook.
- Pen test + threat-model review before launch; ongoing dependency scanning.
- Vendor rule: **no vendor without either a BAA (health-touching) or a DPA + no-data-sale terms (everything else)**. No ad-tech, no third-party behavioral analytics on client surfaces (self-hosted, cookieless analytics only).

## 11.4 What requires legal/compliance review before build

1. Covered-entity / hybrid-entity determination and BAA inventory.
2. Minor consent, parental access, and youth messaging policies.
3. Record-retention schedule per record type (clinical vs. social services vs. housing-funder rules).
4. Mandatory-reporting disclosures and staff protocols in digital channels.
5. Subpoena/legal-request response policy.
6. HIV-data handling under California law.
7. Volunteer confidentiality agreements and background-check policy.
8. Terms of service / privacy policy in plain language + Spanish.

## 11.5 What cannot be determined from public sources

Current systems and their compliance status; existing policies; whether any data has contractual strings (HMIS participation for housing programs would impose HUD data standards — plausible given the CoC history **[INFERENCE]**); insurance/billing workflows; staff device management posture.

---

# SECTION 12 — UX/UI DESIGN PRINCIPLES

**Visual tone.** Warm desert-modern: sunrise gradients used sparingly, generous whitespace, rounded but adult typography; trans-flag palette available as an *opt-in accent theme*, never forced (stealth default is neutral sage/sand). Photography: real community imagery only with documented consent; illustrations otherwise. Feels like a well-designed wellness app, not a government form and not a rainbow sticker.

**Accessibility standards.** WCAG 2.2 AA minimum: 4.5:1 contrast, full screen-reader semantics, 44px touch targets, dynamic type support, reduced-motion mode, captions on all video, plain-language reading level (~6th–8th grade), keyboard-complete staff console. Test with disabled community members, not just audit tools (disability is explicitly in scope per the client's own framing of vulnerable users).

**Language principles.** Ask pronouns, then *use* them in every generated sentence. Never require honorifics or gendered titles. "Chosen name" not "preferred name" (preference implies optional). Explain every sensitive question inline ("Why we ask"). Spanish at parity from MVP (not machine-translated afterthought) **[INFERENCE: essential for this service region]**. No clinical jargon without a plain gloss; no euphemisms that hide meaning.

**Notification rules.** Opt-in per category; neutral by default ("You have an update"); explicit mode only after an interstitial explaining risks; quiet hours honored; nothing sensitive in email subjects; SMS sender is a plain number by default, org-branded only on request; every notification deep-links behind the app lock.

**Form design.** One question per screen on mobile for sensitive topics; save-and-resume always; progress honesty ("3 short sections"); optional fields visibly optional; error states never blame ("We couldn't verify that — want to try another way?"); no dead ends — every form ends with "what happens next, and when."

**Error-message principles.** Say what happened, what we did, what the user can do; never expose internals; never lose entered data; crisis-adjacent surfaces degrade to static cached content rather than failing blank.

**Safety copy examples.**
- Onboarding: "You can use this app without telling us your legal name. Some services (like insurance billing or court paperwork) will need it later — we'll ask only then, and we'll tell you why."
- Shared-device: "Using someone else's phone? Tap here for a private session that erases itself when you close it."
- Crisis banner: "We check messages during business hours. If you're in danger right now, these lines answer 24/7 →"
- Youth disclosure: "Before you share: our staff are required by law to report certain kinds of abuse to keep young people safe. Here's exactly what that means →"

**Onboarding principles.** Value before identity (browse first, sign up when *you* need to); safety features demonstrated interactively (practice the quick exit once); consent unbundled (no "I agree to everything" wall); skippable everything; a returning-user fast path.

---

# SECTION 13 — MVP DEFINITION

**MVP goal.** Replace phone/email-only intake with a safe digital front door, and give staff one queue + one case timeline — measurably cutting time-to-first-contact and manual re-entry, for two launch programs: **free mental wellness** and **gender-affirming hair removal** (the two highest-volume, clearest-workflow public offerings), plus logged-out crisis/resource pages.

**MVP user groups.** Clients (adults only at MVP — youth flow awaits legal signoff), intake staff, navigators for the two launch programs, one admin. Donors/volunteers/leadership dashboards: not in MVP (donation links simply point to the existing processor page).

**MVP features.**
1. Public, logged-out: services info, locations, verified emergency-resource page (offline-cached), plain-language privacy page, "Need help now" routing.
2. Client accounts: chosen-name-first profile, PIN lock, quick exit, consent center v1, notification prefs (neutral-only at MVP).
3. Unified intake wizard with urgency flag + two service-request types (mental wellness, hair removal) + generic "other help" catch-all routed to staff.
4. Appointment *requests* (not self-booking) + staff confirm + reminders (neutral) + reschedule.
5. Secure messaging (client ↔ assigned staff), thread assignment, audit-logged.
6. Staff console: intake queue with triage lanes, case timeline (notes, tasks), request/waitlist board, CSV export of de-identified monthly counts.
7. RBAC v1 (intake / navigator / admin), SSO+MFA, audit log, field-level encryption for T3.
8. English + Spanish.

**Explicitly not in MVP.** Native app-store apps (ship a PWA; evaluate native at Phase 3), youth accounts, donor/volunteer portals, events module (keep Eventbrite temporarily), full resource directory CMS (a curated static emergency list only), leadership analytics, EHR integration, outcome surveys, telehealth video (link out to existing tool), document vault beyond basic upload-to-request.

**Technical architecture (MVP).** PWA (Next.js/React + TypeScript) → REST/tRPC API (Node or Django) → Postgres with row-level security → hosted on a HIPAA-eligible platform with BAA (e.g., AWS with BAA via Lightsail-avoided/ECS+RDS, or Aptible/Healthie-style managed; see §15) → Twilio (BAA) for SMS, Postmark/SES (BAA-eligible) for email → S3-compatible encrypted storage → self-hosted Plausible/Umami analytics (public pages only).

**Staff workflow at launch.** Phone/walk-in intakes get keyed into the same queue (a 60-second staff form) so the queue is the *single* source of truth from day one; old channels feed the new system rather than competing with it.

**Launch requirements.** Legal review complete (§11.4 items 1–4 minimum); privacy policy published; staff trained (2 sessions + sandbox); community soft-launch with 10–20 invited clients; incident-response contact live; Spanish content reviewed by a human; accessibility audit passed; pen test passed.

**Success metrics (first 90 days post-launch).** ≥40% of new intakes arrive digitally; median time-to-first-contact < 2 business days (baseline measured in Phase 0); ≥70% of digital requesters reach "first appointment or referral" without a phone call; staff report ≥30% less duplicate data entry (survey); zero P1 privacy incidents; client satisfaction pulse ≥4/5; quick-exit and PIN adoption tracked (target: offered to 100%, adopted by choice).

**Risks.** Staff adoption (mitigate: co-design, queue replaces — not duplicates — old inboxes); legal review delays youth/EHR scope (mitigate: adults-only MVP); funding gap mid-build (mitigate: phased contracts, open-source components); demand spike beyond capacity (mitigate: honest waitlist UX from day one).

**Timeline estimate.** Phase 0 discovery 4–6 weeks → MVP build 14–18 weeks → soft launch 4 weeks → public launch. **~6–7 months** end to end with a small senior team.

**Budget tiers.**
- **Scrappy (~$60–110K):** 2 senior contractors + fractional design + fractional compliance consult; PWA on managed HIPAA-eligible hosting; heavy use of open-source; org staff do content. Risk: bus factor, slower.
- **Moderate (~$150–250K):** small agency or 3–4 person team, dedicated designer, formal pen test, Spanish localization professionally done, 6 months post-launch support. **Recommended target.**
- **Robust (~$300–500K):** adds native iOS/Android, EHR integration groundwork, 12-month support/SRE, SOC 2-track hardening, research-grade usability program. Only sensible if a dedicated tech grant materializes.

---

# SECTION 14 — FULL ROADMAP

**Phase 0 — Discovery & stakeholder validation (4–6 wks).** Goals: verify every [UNKNOWN]; map real workflows, systems, funder report fields; co-design sessions with TGI community members (paid participation); legal/compliance determinations. Dependencies: leadership sponsorship; counsel engaged. Risks: discovery reveals a bought tool fits better (that's a success, not a failure — see §20). Staffing: product lead, designer/researcher, compliance consultant. Effort: ~6 person-weeks. Success: signed-off requirements, data-governance memo, baseline metrics (call volume, time-to-first-contact, report prep hours).

**Phase 1 — MVP (14–18 wks + 4 wk soft launch).** As specified in §13. Staffing: 2 engineers, 1 designer, PM/product lead (fractional), compliance advisor. Success metrics: §13.

**Phase 2 — Staff workflow expansion (8–12 wks).** Goals: bring housing, legal-navigation, and HIV-linkage programs onto the platform; referral tracker; document checklists/vault v2; resource-directory CMS + verification queue; waitlist transparency; supervisor views. Dependencies: MVP adoption proven; program leads engaged; HIV-data legal review done. Risks: program-specific funder data rules (HMIS!) complicate schema — resolve via integration/export rather than replication. Staffing: same team + part-time program liaison. Effort: ~30 person-weeks. Success: ≥80% of new cases across programs live in-platform; referral follow-up overdue rate cut 50%.

**Phase 3 — Community, events, donors, volunteers (8–12 wks).** Goals: events module replaces Eventbrite (public calendar, private RSVP, check-in); volunteer shifts + hours; donor campaign pages via processor integration (walled domain); youth flow **if** legal signoff obtained; native app wrappers if stealth research demands them. Dependencies: comms team capacity; counsel youth memo. Risks: youth safeguarding; donor-data wall discipline. Effort: ~28 person-weeks. Success: Trans Pride 2027 (or next cycle) run end-to-end on platform with auditable attendance; volunteer hours auto-reported; first $ raised through campaign pages.

**Phase 4 — Analytics, outcomes, integrations (10–14 wks).** Goals: leadership dashboard with k-anonymized trends; funder report templates (CDPH TGI Fund first); consented outcome check-ins; EHR/calendar/telehealth integrations as validated; findhelp API feed into directory review queue. Dependencies: 12+ months of clean data; funder field mapping from Phase 0 kept current. Risks: dashboard temptation to over-collect — governance board reviews every new metric. Effort: ~32 person-weeks. Success: quarterly funder reporting time cut ≥70%; outcome data cited in ≥2 grant applications.

**Phase 5 — Regional network/platform model (exploratory).** Goals: multi-tenant or white-label offering to peer TGI-serving orgs (TH&WC already spans 3 counties; peers statewide face identical tooling gaps — and the CDPH TGI Fund explicitly funds TGI-serving org capacity, AB 2218). Options: open-source the core with hosted offering; consortium governance. Dependencies: Phases 1–4 stable; dedicated funding; appetite for being a platform steward. Risks: mission drift, support burden, federated privacy complexity (each tenant = isolated data). Success: 1–2 partner orgs piloted; sustainability plan (grants + modest SaaS fees) covering maintenance.

---

# SECTION 15 — TECHNICAL ARCHITECTURE

**Reference architecture (either option):**

```
[Client PWA / (later) native wrappers]      [Staff web console]
              \                                   /
               ├── API gateway (authn, rate limit)
               ├── App services: intake • scheduling • messaging •
               │   directory • events • notifications • reporting
               ├── Policy engine (RBAC × program × consent) — server-side only
               ├── Postgres (RLS; field-level envelope encryption for T3)
               ├── Object storage (encrypted docs)
               ├── Async jobs (reminders, purges, report builds)
               ├── Notification service (template registry, neutral-safe classing)
               ├── Append-only audit store
               └── Integrations edge: SMS(Twilio+BAA) • email(BAA-eligible) •
                   payments(walled) • video link-out • calendar sync •
                   findhelp API • (later) EHR via FHIR
Observability: structured logs (PII-scrubbed), uptime probes, error tracking (self-hosted Sentry/GlitchTip)
Backups: encrypted nightly + point-in-time; quarterly restore drills
Compliance logging: access reviews, retention-job reports, export ledger
```

**Component choices.** Frontend: React/Next.js PWA (TypeScript), offline-cache for emergency pages; design system tokens for stealth/affirming themes. Backend: Node (NestJS/tRPC) or Django — pick per implementing team's strength; boring beats novel. DB: Postgres + row-level security. Auth: passkeys + OTP for clients; SSO (Google/Microsoft) + MFA for staff — via a vendor that signs BAAs (e.g., Auth0/AWS Cognito) or self-hosted (Keycloak/Zitadel). CMS for resources/education: headless (Payload/Strapi) or built-in admin. Analytics: self-hosted Plausible/Umami, public pages only; product analytics = first-party event counts, no third-party SDKs.

### Option A — Low-cost nonprofit stack
Managed platform with BAA: **Supabase (HIPAA add-on) or Aptible**, Next.js on the same platform or Vercel *for public pages only* (no PHI through non-BAA infra), Twilio + AWS SES (BAA), Stripe/Givebutter for the walled donor domain, GitHub Actions CI.
- *Pros:* fastest to ship; least ops burden; cheap ($300–800/mo infra); nonprofit credits often available; small team can run it.
- *Cons:* platform limits on fine-grained network controls; vendor dependence; field-level encryption is DIY on top; some auditors prefer classic cloud.
- *Complexity:* low-moderate. *Privacy/security:* strong **if** BAAs signed and RLS + envelope encryption implemented rigorously; the platform doesn't absolve app-layer discipline. *Maintenance:* ~0.25–0.5 FTE.

### Option B — Healthcare-grade stack
**AWS with BAA**: ECS/Fargate services, RDS Postgres (KMS), S3 + Object Lock for audit/WORM, Cognito, CloudTrail/GuardDuty/Config, WAF, VPC isolation, Terraform IaC; optionally **Medplum** (open-source FHIR backend) as the clinical-adjacent data core to ease future EHR interop.
- *Pros:* audit-friendly; granular controls; scales to Phase 5 multi-tenant; FHIR path future-proofs clinical integration; no single-vendor app platform lock-in.
- *Cons:* real DevOps burden; slower initial build; $1–2.5K/mo infra + engineering time; overkill for MVP volumes.
- *Complexity:* high. *Privacy/security:* ceiling is higher; floor depends entirely on configuration discipline. *Maintenance:* 0.5–1 FTE or managed-services contract.

**Recommendation.** Start on Option A with clean domain boundaries and IaC habits so a Phase 4/5 migration to Option B is a port, not a rewrite. Never route PHI through non-BAA components regardless of option.

---

# SECTION 16 — INTEGRATIONS

| Integration | Why it matters | Risks | Safer alternative | MVP priority |
|---|---|---|---|---|
| Website CMS (trans.health, WordPress-typical **[INF]**) | Single source for service info; deep links into app | Plugin sprawl; PHI must never touch the marketing site | Keep marketing site read-only; app hosts all forms | **MVP** (links only) |
| Google Workspace / M365 SSO | Staff auth, MFA, offboarding in one place | Mis-scoped OAuth | SSO for staff only; clients never Google-auth (metadata trail) | **MVP** |
| Calendar sync (staff) | Staff live in their calendars | Event titles leaking client info | One-way sync, privacy-safe titles | Phase 2 |
| SMS (Twilio + BAA) | Reminders/OTP for phone-first clients | Message content exposure; carrier filtering | Neutral templates only; registered 10DLC | **MVP** |
| Email (SES/Postmark, BAA-eligible) | Receipts, magic links | Subject-line leaks; household inbox access | Neutral subjects; in-app-first strategy | **MVP** |
| Telehealth video (Zoom for Healthcare / Doxy.me) | Free MH program is telehealth (GuideStar) | Non-BAA video tools | Link-out to org's BAA'd tool; don't build video | **MVP** (link-out) |
| EHR/EMR (whichever the clinic uses **[UNKNOWN]**) | Kill double data entry for clinic staff | Deepest PHI risk; brittle interfaces | Phase-gated; reference-not-replicate; FHIR if available | Phase 4 |
| Donation processor (Stripe / Givebutter) | Existing online giving continues | PCI scope; donor-client linkage temptation | Hosted checkout; walled donor domain | Phase 3 |
| CRM (donor-side, e.g., Bloomerang) | Development team workflows | Same linkage risk | Sync campaign totals only, not client anything | Phase 3 |
| Volunteer platforms (TurnOut/Idealist) | Existing recruitment channels (both list TH&WC) | Duplicate rosters | Keep as top-of-funnel links into platform onboarding | Phase 3 |
| findhelp.org API | Seed/refresh resource directory | Unvetted listings dangerous for trans users | Feed a staff review queue, never auto-publish | Phase 2 |
| Grant reporting (funder portals; possible HMIS for housing **[UNKNOWN]**) | Reporting is a top pain | HMIS has its own data standards & privacy regime | Export adapters per funder; keep HMIS data in HMIS | Phase 4 |
| Maps | Directions to 4–5 sites | Third-party trackers on embedded maps | Static maps / OSM tiles; no location permission requests | Phase 2 |
| Identity verification | Almost never needed | Exclusionary + surveillance risk for exactly this population | Don't. Staff verify identity contextually when legally required | Never (default) |
| Analytics | Improve UX, prove reach | Third-party SDKs leak by design | Self-hosted Plausible/Umami; first-party counts; no client-surface tracking | **MVP** (public pages) |

---

# SECTION 17 — GRANT AND FUNDING ALIGNMENT

**How the platform supports funding operations.**
- **Grant reporting:** unduplicated client counts, service units, county splits, and demographic aggregates generated from operational data — directly matching the shape of CDPH TGI Fund reporting (the org is an existing grantee — lachealthequity.substack.com; CDPH) and typical county/foundation formats.
- **Outcome measurement:** consented check-ins convert "we served 400 people" into "68% of housing clients remained stably housed at 6 months" — the difference between renewal and non-renewal in competitive cycles.
- **Service-demand evidence:** waitlist and unmet-request trends give leadership hard numbers for advocacy — acutely relevant while contesting the Riverside County contract language (KESQ Dec 2025) and replacing lost federal-facing revenue (trans.health/notice).
- **Donor communication & storytelling:** campaign pages fed by real aggregates; impact digests that never expose individuals.
- **Volunteer-hour tracking:** auto-summed hours are both a match-value line item in many grants and a community-engagement metric.
- **Program evaluation:** managers see which pathways stall, informing staffing asks in proposals.
- **Health-equity alignment:** county-level dashboards map to regional health-equity framing used by California funders.

**Funding angles to research (categories, not promises).**
1. **California TGI-specific funds:** CDPH TGI Wellness and Equity Fund rounds (existing relationship; AB 2218; successor bills like AB 1487 signal ongoing appropriations — legiscan) — platform = capacity-building + service-access infrastructure.
2. **Digital health equity / telehealth access:** state and foundation programs funding technology that removes access barriers for underserved populations (the free telehealth MH program is a natural hook).
3. **LGBTQ+ health foundations:** e.g., regional LGBTQ+ funds and national LGBTQ-health funders — research current cycles.
4. **HIV/STI prevention:** the org does HIV education/linkage (trans.health); linkage-to-care digital tooling fits prevention-portfolio logic (Ending the HIV Epidemic-adjacent state/county streams — verify current availability given federal volatility).
5. **Behavioral health access:** county MHSA-lineage (now BHSA) innovation/community funds in Riverside/San Diego counties — digital front doors for underserved populations are a recognized category. **Verify current program names/cycles.**
6. **Youth support & safety:** foundations funding LGBTQ+ youth crisis prevention (only once the youth flow is counsel-approved).
7. **Legal access:** access-to-justice/tech grants for the name/gender-marker workflow.
8. **Housing navigation:** state (non-federal) housing funds and private funders — pointedly relevant while HUD-linked money is constrained for this org.
9. **Accessibility & multilingual access:** funders supporting language justice and disability inclusion could underwrite the Spanish parity and WCAG work as discrete line items.
10. **Corporate/community partners:** the org already runs an employment-themed Pride event with employer participation (Empower and Employ — KESQ) — sponsorship of the platform's employment module is a natural corporate ask; it is also a Desert Business Association member.

**Positioning rule:** pitch the platform as *service-delivery infrastructure with measurable access outcomes*, never as "an app project." Funders buy reduced wait times, safer access, and auditable impact.

---

# SECTION 18 — RISK REGISTER

Severity/Likelihood: H/M/L. Owner = accountable role once launched.

| Risk | Sev | Lik | Mitigation | Owner | Design implication |
|---|---|---|---|---|---|
| **User outing** via notifications, shared devices, or visible app | H | M | Neutral-by-default comms; stealth label; PIN; quick exit; onboarding safety drill | Product + Privacy officer | Template registry with "neutral-safe" gate; no content previews anywhere |
| **Data breach → mass exposure of TGI identities/health data** | H | M | Minimization; T3 field encryption; BAAs; pen tests; purge jobs; IR plan with community-sensitive comms | Exec + security lead | Don't store what you can't defend; audit WORM store |
| **Legal compulsion / hostile audit** (cf. county "gender ideology" contract climate — KESQ 12/2025) | H | M | Retention schedules actually executed; counsel-reviewed subpoena runbook; data segregation by program/funder | Exec + counsel | Deletable-by-design records; funder-scoped exports; no speculative data |
| **Staff overload / non-adoption** | H | H | Co-design; queue replaces old inboxes; measure time saved; manager dashboards | Program managers | Staff console optimized for 60-second tasks; phone intakes enter same queue |
| **Scope creep** | M | H | Module roadmap with phase gates; every new field needs purpose+tier+retention | Product lead | Form engine enforces field governance |
| **Compliance ambiguity (hybrid entity, minors, HMIS)** | H | M | Phase-0 legal determinations before schema freeze; adults-only until youth memo | Exec + counsel | Feature flags for youth/HIV/housing modules |
| **Inaccurate resource listings endanger users** | H | M | Verified-on dates; re-verification SLAs; staff-only publishing; community flag button | Directory admin | Stale listings auto-demote to "unverified" |
| **Crisis misuse / mistaken rescue expectations** | H | M | Persistent honest response-time copy; crisis rails on every MH surface; staff protocol for flagged intakes | Clinical lead | Crisis routing works logged-out + offline |
| **Notification/channel leakage** | H | M | Per-channel consent; quiet hours; neutral SMS sender | Product | No third-party push metadata (self-host push where feasible) |
| **Shared-device compromise** | H | M | App lock, session timeouts, remote sign-out, private-session mode | Product | No "remember me" default on unregistered devices |
| **Misgendering by the system** | M | M | Chosen-name-first schema; pronoun-aware copy engine; staff console shows pronouns everywhere | Product + QA | Legal name renders only in purpose-gated views |
| **Inaccessible design excludes disabled users** | M | M | WCAG 2.2 AA gate in CI; paid testing with disabled community members | Design lead | Reduced-motion, dynamic type, SR-complete |
| **Low client adoption** | M | M | Soft-launch with trusted community members; staff champion program; posters/QR at sites & events | Comms | Value without login; zero-friction first request |
| **Vendor lock-in** | M | M | Open standards (Postgres, FHIR later), IaC, export tooling from day one | Tech lead | Domain boundaries designed for portability |
| **Underfunded maintenance** | H | M | Budget 20–25% of build cost/yr; pursue multi-year capacity grants; consider Phase-5 consortium sharing | Exec | Boring stack, few services, managed platform |
| **Community mistrust after any incident** | H | L→M | Published plain-language privacy model; client-visible access history; rapid honest disclosure culture | Exec | Trust features are product features |
| **Law/policy changes (state or federal)** | H | H (climate) | Modular compliance flags; counsel on retainer; scenario plans (e.g., data-hostile federal rules) | Exec + counsel | Ability to tighten collection/retention per module quickly |
| **Harassment/malicious use (fake intakes, event probing)** | M | M | Rate limits; RSVP privacy; venue-reveal gating; moderation queue; no public member lists | Ops | Abuse-report affordances; block/allow tooling |

---

# SECTION 19 — VALIDATION PLAN

**Leadership discovery interviews (Phase 0).** Sample questions: Where does staff time actually go in a week? Which funder reports hurt most, and can we see (redacted) templates? What systems exist today for clinic, MH, housing, donors — and what do they cost? What is your covered-entity determination? What happened operationally when the county contract ended, and what evidence would have helped? What's the 3-year growth thesis — more counties, more programs, or deeper service? Who owns technology decisions and maintenance budget?

**Staff workflow sessions (per program).** Shadow intake for a day (with all client interactions consented/anonymized); map a real (de-identified) client journey across programs; ask: what do you re-type more than once? What do you track in your head because no system holds it? What would make you *not* use a new tool?

**Client/community listening (paid participants, recruited via org channels).** Not usability yet — needs and fears: How did you first reach TH&WC, and what almost stopped you? What does "safe" mean on your phone? Who must never see that you use this service? Which name/pronoun handling failures have you experienced elsewhere? Would you use waitlist visibility, messaging, reminders — and on which channel?

**Privacy/safety testing (pre-launch).** Red-team the household-adversary scenario (device inspection walkthrough); notification-leak audit across lock screens/watches/car displays; quick-exit timing tests; subpoena tabletop with counsel; break-glass audit drill.

**Usability testing.** 8–12 TGI community members across age/language/tech-comfort; tasks: first request, reschedule, find emergency housing resource logged-out, practice quick exit; measure completion, time, and *felt safety* (post-task Likert + interview). Staff console: intake-queue race against the current phone process on realistic volumes.

**Accessibility testing.** Automated (axe) in CI + manual screen-reader passes (VoiceOver/TalkBack) + paid sessions with disabled community testers; Spanish-language testing with native speakers.

**Pilot launch plan.** 4-week soft launch: 10–20 invited clients + full intake staff; weekly debriefs; kill-switch criteria defined in advance (any P1 privacy incident pauses signups); public launch gated on pilot metrics.

**Feedback channels post-launch.** In-app feedback (optional, anonymous-capable); quarterly community advisory board (paid TGI members) reviewing metrics *and* any proposed new data collection; staff retro monthly; public changelog.

**Success metrics.** As §13 plus: % staff using console daily; funder-report prep hours; directory freshness (% verified <90 days); advisory-board continuity.

**Must be validated before build (hard gates).** Covered-entity/BAA determination; adults/youth scope decision; the two MVP programs' real workflows; funder report field inventory; baseline metrics; community appetite for accounts vs. anonymous flows; Spanish-language requirement scope; hosting/vendor list approved by counsel.

---

# SECTION 20 — FINAL RECOMMENDATION

## 20.1 Best app concept
**Oasis by TH&WC**: a stealth-capable, chosen-name-first PWA front door for clients (request services, track care, message navigators, find verified resources, join community) fused with a single staff console (triage queue, case timeline, referrals, scheduling) and privacy-preserving reporting. It succeeds precisely because TH&WC already operates the full stack of services organizationally (trans.health; GuideStar) — the software's job is to make that integration real for clients and staff.

## 20.2 Highest-priority MVP features
1. Unified intake + urgency triage (24/7 async front door).
2. Staff intake queue + case timeline (replaces phone-tag and re-keying).
3. Appointment requests + neutral reminders for hair removal & free mental wellness.
4. Secure messaging with assigned staff.
5. Stealth basics: PIN lock, quick exit, neutral notifications, chosen-name-everywhere.
6. Logged-out verified emergency resources (offline-cached) + honest crisis routing.
7. De-identified monthly service-count export.

## 20.3 Features to avoid initially
Youth accounts (until counsel memo), EHR integration, custom video, donor CRM depth, public forums/social feeds (moderation risk), open self-booking, native app-store builds, any analytics SDK on client surfaces, geolocation features, and identity verification of any kind.

## 20.4 Build-versus-buy
**Hybrid.** *Buy/keep:* payments (Stripe/Givebutter), telehealth video (existing BAA'd tool), staff email/SSO (Workspace/M365), donor CRM if one exists, accounting, and possibly a nonprofit case-management backend if discovery reveals one already embedded (then the build narrows to the client-facing safety layer + integration). *Build:* the client-facing experience (no off-the-shelf product delivers stealth-grade, chosen-name-first, multi-program UX), the consent/permission engine, and the thin staff console — unless Phase 0 shows an incumbent system staff already trust, in which case build the front door and integrate. **Decision gate lives in Phase 0, on evidence, not preference.**

## 20.5 First 90 days
Weeks 1–2: engage counsel (covered-entity + minors memos); appoint internal product owner; convene paid community advisory board. Weeks 3–6: discovery interviews, workflow shadowing, systems/funder-field inventory, baseline metrics. Weeks 7–8: synthesis; build-vs-buy decision; architecture choice (default: Option A); budget tier locked; funding applications drafted (TGI Fund capacity angle + one foundation). Weeks 9–12: design sprints with community testing of intake + stealth flows; schema + data-governance sign-off; development starts on the MVP slice.

## 20.6 Open questions for stakeholder interviews
1. What is the legal structure of clinic vs. social programs, and the current HIPAA determination?
2. Which systems (EHR, case management, HMIS, donor CRM, scheduling) are in use today, under which contracts?
3. Authoritative list of sites, programs, staffing, and current wait times?
4. Do you serve minors in mental wellness, and under what consent protocol?
5. Which funder reports are due, on what fields and cycles (CDPH TGI Fund and beyond)?
6. What did the Riverside County contract require operationally, and what data would strengthen the current complaint and future contracting (KESQ Dec 2025)?
7. What are call volumes, no-show rates, and time-to-first-contact today?
8. What languages do clients actually need? What share are Spanish-dominant?
9. What is the realistic annual budget for technology maintenance?
10. Who internally will own this product long-term?
11. What community-trust commitments (data promises) is leadership willing to publish and be held to?
12. Is there appetite, eventually, to share the platform with peer TGI-serving organizations (Phase 5)?

## 20.7 Funder-ready pitch (one paragraph)
> The Transgender Health and Wellness Center is Southern California's largest trans-led nonprofit, serving TGI communities across Riverside, San Bernardino, and San Diego counties with gender-affirming clinical care, free mental health services, housing, legal, and employment support. Today, every one of those services is reached by phone call during business hours. Oasis — our privacy-first digital front door — will let any community member safely request help 24/7 under their chosen name, track their care, and reach trusted resources, while cutting staff administrative time and producing the rigorous, de-identified outcome data our public and private funders require. Built with and for our community, with stealth-grade safety for people who are not yet out, Oasis turns our proven wraparound model into infrastructure: faster access, safer contact, stronger evidence, and a platform our peer organizations can one day share.

---

*End of strategy document. All organizational facts cited to sources in Part A.2; inferences and unknowns labeled throughout. This document contains no information about, and was produced without collecting any information on, individual clients, donors, volunteers, or community members.*
