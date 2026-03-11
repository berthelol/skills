# LinkedIn API Endpoints

Base path: `/v1/linkedin`

## Profiles & Companies

### Person's Profile
```
GET /v1/linkedin/profile?handle={username}
```
Public profile data including recent posts. Only returns publicly visible information (what you'd see in incognito mode). Note: work history and job titles may be unavailable due to LinkedIn restrictions.

### Company Page
```
GET /v1/linkedin/company?handle={company_slug}
```
Public company page data.

### Company Posts
```
GET /v1/linkedin/company/posts?handle={company_slug}&cursor={cursor}
```
Posts from a company page. **Limited to 7 pages total** (LinkedIn restriction).

## Posts

### Post Details
```
GET /v1/linkedin/post?url={post_url}
```
Details for a specific LinkedIn post or article, including transcript if it's a video.

## Ad Library

### Search Ads
```
GET /v1/linkedin/ads/search?query={keyword}&cursor={cursor}
```
Search the LinkedIn Ad Library for ads by keyword.

### Ad Details
```
GET /v1/linkedin/ad?ad_id={id}
```
Full details for a specific ad, including video and carousel images.

## Notes

- LinkedIn is restrictive about data access — some fields may not be available
- Company posts max out at 7 pages (LinkedIn's limitation)
- Profile data is limited to what's publicly visible in incognito mode
- Ad library endpoints support video and carousel image retrieval
- Use `trim=true` to reduce response size
