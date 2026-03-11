# Instagram API Endpoints

Base path: `/v1/instagram` (some endpoints have v2 versions)

## Profile & User Data

### Get Profile
```
GET /v1/instagram/profile?handle={username}
```
Returns public profile data, recent posts, and related accounts.

### Basic Profile
```
GET /v1/instagram/profile/basic?user_id={id}
```
Lightweight profile lookup by user ID.

## Content

### User Posts
```
GET /v1/instagram/user-posts?handle={username}&cursor={cursor}
```
Paginated list of a user's public posts.

### Post/Reel Info
```
GET /v1/instagram/post?url={post_url}
```
Full details for a single post or reel: likes, comments, caption, media URLs.

### Reels
```
GET /v1/instagram/reels?handle={username}&cursor={cursor}
```
All public reels from a profile.

### Transcript (v2)
```
GET /v2/instagram/media/transcript?url={post_url}
```
Transcript of an Instagram video post or reel. Note: this is a v2 endpoint.

### Embed HTML
```
GET /v1/instagram/embed?handle={username}
```
HTML embed code for a user's profile.

## Story Highlights

### Story Highlights
```
GET /v1/instagram/highlights?handle={username}
```
List of story highlight collections from a user.

### Highlight Details
```
GET /v1/instagram/highlight?highlight_id={id}
```
Contents of a specific story highlight.

## Search

### Search Reels (v2)
```
GET /v2/instagram/reels/search?query={keyword}&cursor={cursor}
```
Search reels by keyword. Costs 1 credit per 10 reels, max 60 reels. Requires manual pagination.
Note: v1 version is being deprecated — use v2.

## Comments

### Post Comments (v2)
```
GET /v2/instagram/post/comments?url={post_url}&cursor={cursor}
```
Comments on a post or reel. Requires manual pagination.
Note: v1 version is being deprecated — use v2.

## Deprecated

- **Reels using Song** — deprecated endpoint, no longer available.

## Notes

- v2 endpoints require manual pagination (pass cursor yourself)
- v1 convenience endpoints that auto-paginate are being phased out (deprecated as of Feb 2026)
- Use `trim=true` to reduce response size
