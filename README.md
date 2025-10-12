## 🎮 E-Sports Project — MySQL Database Structure

**Database:** `classworks6_db`  
**Tables Count:** 22  
**Storage Engine:** MyISAM  
**Collation:** latin1_swedish_ci  

---

### 🟥 Tier 1 — Core Functional Tables (Main Game Logic)
| Table | Description |
|--------|-------------|
| `players` | Stores player profiles — name, username, role, total points, etc. |
| `teams` / `Teams` | Contains team information (name, tag, logo, rank). |
| `matches` / `Matches` | Details of each match — teamA vs teamB, schedule, and result. |
| `Player_Scores` | Stores individual player stats for every match (kills, runs, assists, etc.). |
| `Players_Teams` | Junction table linking players to their respective teams. |
| `Tournaments` / `tournaments` | Defines tournament details — name, start date, prizes, and status. |
| `Tournaments_Players` | Mapping table of players registered in tournaments. |
| `live_tournaments` | Real-time data of ongoing tournaments and live status. |
> 🧠 *These tables are the “engine room” of your esports system — all gameplay and scoring logic depends on them.*

---

### 🟧 Tier 2 — Support & Analytics Tables
| Table | Description |
|--------|-------------|
| `leaderboard` | Dynamic ranking system showing top players or teams. |
| `achievements` | Stores unlocked milestones, badges, and achievements for users. |
| `match_history` | Historical data of past matches for statistics and replay tracking. |
| `Game_Scores` | Global or per-game cumulative scores and summaries. |
> ⚙️ *These enhance the analytics layer and power leaderboards, history views, and reports.*

---

### 🟨 Tier 3 — Communication & Interaction Tables
| Table | Description |
|--------|-------------|
| `Chat_Logs` | Chat data between users or teams within tournaments or lobbies. |
| `notifications` | Stores alerts, match updates, and event messages for users. |
| `reports_feedback` | Player-submitted feedback or issue reports. |
| `reports` | System-generated or admin-submitted reports (statistics, logs). |
> 💬 *Handles user communication, moderation, and engagement.*

---

### 🟩 Tier 4 — Administrative & Meta Tables
| Table | Description |
|--------|-------------|
| `Admins` | Admin credentials, roles, and privileges for backend management. |
| `users` | Base user authentication, registration, and access roles. |
| `rewards` | Reward and bonus data associated with achievements or tournaments. |
> 🧑‍💼 *These tables control system permissions, rewards, and overall configuration.*

---

### ✅ Summary
| Tier | Category | Purpose |
|------|-----------|----------|
| 🟥 **Tier 1** | Core Functional | Gameplay logic, scoring, tournaments |
| 🟧 **Tier 2** | Support / Analytics | Statistics, achievements, and history |
| 🟨 **Tier 3** | Communication | Chat, notifications, feedback |
| 🟩 **Tier 4** | Admin / Meta | Access, authentication, rewards |
---

### 💾 Notes
- **Primary Keys:** Each major table (players, teams, matches) should include an `AUTO_INCREMENT` integer ID.  
- **Foreign Keys:** Although MyISAM does not enforce FKs, maintain consistent naming (e.g., `player_id`, `team_id`, `match_id`) for relational clarity.  
- **Indexes:** Recommended on `player_id`, `team_id`, `tournament_id`, and `match_id` for faster queries.  

---

> **Next:** Combine this MySQL section with your MongoDB (E-Commerce) and PostgreSQL (E-Learning) schemas to finalize the complete `README.md` database documentation.







///////////////////////////////////////////////////////////////////////////////////////////////////////







## 🛒 E-Commerce Project — MongoDB Database Structure

**Database:** `ecommerce_db`  
**Type:** NoSQL (Document-based)  
**Driver/ODM:** Mongoose / MongoDB Native Driver  

---

### 🟥 Tier 1 — Core Collections (Business Logic)
| Collection | Description |
|-------------|-------------|
| `users` | Stores all registered user profiles including authentication and roles. |
| `products` | Product catalog containing title, description, price, stock, category, and images. |
| `orders` | Contains order details such as ordered items, total price, payment status, and user reference. |
| `cart` / `carts` | Temporary user cart storage before final order placement. |
| `categories` | Product grouping with tags, meta info, and filtering support. |
> 🧠 *These collections define the backbone of the e-commerce system — users, products, and orders.*

---

### 🟧 Tier 2 — Transactional & Analytics Collections
| Collection | Description |
|-------------|-------------|
| `payments` | Stores payment gateway responses, transaction IDs, and order references. |
| `shipments` | Tracks shipment details — courier info, status, and delivery timelines. |
| `invoices` | Auto-generated billing documents mapped to each order. |
| `coupons` | Promotional codes with validity and discount logic. |
| `reviews` | Customer feedback, ratings, and product review metadata. |
> ⚙️ *These collections enhance order lifecycle, analytics, and marketing tools.*
---

### 🟨 Tier 3 — User Interaction & Support Collections
| Collection | Description |
|-------------|-------------|
| `wishlists` | Stores user-favorite products for later purchase. |
| `notifications` | System-generated messages, order updates, and alerts. |
| `support_tickets` | Customer service queries, complaints, and responses. |
| `activity_logs` | Tracks user activity (searches, clicks, purchases). |
> 💬 *Focused on customer experience, engagement, and support systems.*

---

### 🟩 Tier 4 — Administrative & Meta Collections
| Collection | Description |
|-------------|-------------|
| `admins` | Admin account data and access control information. |
| `inventory` | Backend-level stock management and update logs. |
| `settings` | System-wide configurations (currency, tax, payment methods). |
| `audit_logs` | Security logs for data changes, admin edits, or policy updates. |
> 🧑‍💼 *Ensures secure backend control, auditing, and business management.*

---

### ✅ Summary
| Tier | Category | Purpose |
|------|-----------|----------|
| 🟥 **Tier 1** | Core Collections | Users, Products, Orders |
| 🟧 **Tier 2** | Transactional | Payments, Shipments, Reviews |
| 🟨 **Tier 3** | User Interaction | Wishlists, Notifications, Support |
| 🟩 **Tier 4** | Admin / Meta | Inventory, Settings, Audit Logs |
---

### 💾 Notes
- **Document IDs (`_id`)** are automatically generated `ObjectId`s by MongoDB.  
- **Relationships:** Implemented using reference fields (e.g. `userId`, `productId`) or embedded documents as needed.  
- **Indexes:** Recommended on `email`, `category`, `orderId`, and `productId` for faster lookups.  
- **Schema Management:** Mongoose models should define validation, timestamps (`createdAt`, `updatedAt`), and virtuals for computed fields.  

---

> **Next:** Let’s add the **📚 E-Learnings (PostgreSQL)** schema next in the same markdown pattern to finalize your full multi-database README.md documentation.














//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////



## 📚 E-Learnings Project — PostgreSQL Database Structure

**Database:** `elearnings_db`  
**Type:** Relational (SQL)  
**ORM/Driver:** Prisma / pg-promise / node-postgres (pg)  

---

### 🟥 Tier 1 — Core Academic Tables (Main Learning Engine)
| Table | Description |
|--------|-------------|
| `users` | Base table for all registered accounts (students, instructors, admins). |
| `courses` | Contains course metadata — title, description, duration, and author. |
| `lessons` | Individual lesson units under a course — video, content, or quiz type. |
| `enrollments` | Maps users to the courses they are enrolled in. |
| `progress` | Tracks each user’s lesson completion and percentage progress. |

> 🧠 *These define the core e-learning functionality — users learning courses through lessons and tracking progress.*

---

### 🟧 Tier 2 — Assessments & Academic Analytics
| Table | Description |
|--------|-------------|
| `quizzes` | Each lesson’s quiz questions and answers. |
| `quiz_attempts` | Stores each student’s quiz attempt, score, and timestamp. |
| `assignments` | Practical or written tasks submitted by students per course. |
| `grades` | Final evaluation or cumulative grade per course. |

> 📊 *Focuses on testing, performance analytics, and skill assessment.*

---

### 🟨 Tier 3 — Communication & Interaction Tables
| Table | Description |
|--------|-------------|
| `discussions` | Forum-like posts/comments for each course or lesson. |
| `messages` | Private or instructor-student message threads. |
| `notifications` | Alerts for new courses, assignments, or instructor updates. |
| `feedback` | Student feedback or rating per course/instructor. |

> 💬 *Supports engagement, discussion, and collaboration.*

---

### 🟩 Tier 4 — Administrative & Management Tables
| Table | Description |
|--------|-------------|
| `instructors` | Instructor-specific data — qualifications, experience, and bio. |
| `categories` | Classification of courses by topic (tech, science, language, etc.). |
| `certificates` | Course completion certificates with issue date and unique ID. |
| `settings` | Global configuration table for platform defaults (themes, policies). |
| `reports` | Admin-generated reports for analytics and maintenance. |
> 🧑‍💼 *Enables control, reporting, and institutional-level management.*

---

### ✅ Summary
| Tier | Category | Purpose |
|------|-----------|----------|
| 🟥 **Tier 1** | Core Academic | Users, Courses, Lessons, Enrollments |
| 🟧 **Tier 2** | Assessments | Quizzes, Assignments, Grades |
| 🟨 **Tier 3** | Interaction | Discussions, Messages, Notifications |
| 🟩 **Tier 4** | Admin / Meta | Instructors, Certificates, Reports |

---

### 💾 Notes
- **Primary Keys:** All main tables use `SERIAL` or `BIGSERIAL` with auto-increment IDs.  
- **Foreign Keys:**  
  - `lessons.course_id → courses.course_id`  
  - `enrollments.user_id → users.user_id`  
  - `enrollments.course_id → courses.course_id`  
  - `progress.lesson_id → lessons.lesson_id`  
- **Constraints:**  
  - `UNIQUE (email)` on `users`  
  - `CHECK (progress_percent BETWEEN 0 AND 100)`  
- **Indexes:** Recommended on `course_id`, `user_id`, `lesson_id` for join speed.  
- **Schema:** You can separate academic schema as `public` and admin schema as `management` for modular control.  

---

> **Complete Database Documentation Set:**  

> - 🛒 [E-Commerce (MongoDB)](#e-commerce-project--mongodb-database-structure)  
> - 🎮 [E-Sports (MySQL)](#e-sports-project--mysql-database-structure)  
> - 📚 [E-Learnings (PostgreSQL)](#e-learnings-project--postgresql-database-structure)

---

> ⚡ **Tip:** Together these three databases represent a full-stack multi-domain architecture —  
> combining *NoSQL (MongoDB)* for flexibility, *MySQL* for structured event systems,  
> and *PostgreSQL* for strong relational logic & academic precision.
