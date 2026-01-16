# Setup Guide

## Initial Setup

Follow these steps to set up the automated DMV wait times tracker on GitHub:

### 1. Initialize Git Repository

```bash
cd C:\Users\aiappsgpt\Desktop\dmv
git init
git add .
git commit -m "Initial commit: Texas DMV wait times tracker"
```

### 2. Create GitHub Repository

1. Go to [GitHub](https://github.com/new)
2. Create a new repository (e.g., `texas-dmv-wait-times`)
3. Do NOT initialize with README (we already have one)

### 3. Push to GitHub

```bash
git remote add origin https://github.com/YOUR_USERNAME/texas-dmv-wait-times.git
git branch -M main
git push -u origin main
```

### 4. Configure GitHub Actions Permissions

1. Go to your repository on GitHub
2. Click **Settings** → **Actions** → **General**
3. Scroll down to **Workflow permissions**
4. Select **Read and write permissions**
5. Check **Allow GitHub Actions to create and approve pull requests**
6. Click **Save**

### 5. Test the Workflow

#### Option A: Manual Trigger
1. Go to **Actions** tab in your repository
2. Click on **Update DMV Wait Times** workflow
3. Click **Run workflow** → **Run workflow**
4. Wait for the workflow to complete

#### Option B: Wait for Scheduled Run
The workflow will automatically run daily at 8 AM UTC (2 AM CST)

### 6. Verify the Setup

After the first successful run:
1. Check that `dmv_wait_times.json` appears in your repository
2. View the file to see the extracted data
3. Check the commit history to see automated commits

## Troubleshooting

### Workflow Fails with Permission Error
- Make sure you've enabled **Read and write permissions** in Settings → Actions → General

### No Data Extracted
- Check the Actions logs for error messages
- Verify the Texas DPS website is accessible
- The website structure may have changed (update the parsing logic if needed)

### Python Dependencies Issue
- Ensure `requirements.txt` includes all necessary packages
- Check the Actions logs for specific missing packages

## Customization

### Change Schedule
Edit `.github/workflows/update-dmv-data.yml` and modify the cron expression:

```yaml
schedule:
  - cron: '0 8 * * *'  # Daily at 8 AM UTC
```

Cron format: `minute hour day month day-of-week`

Examples:
- `0 */6 * * *` - Every 6 hours
- `0 12 * * *` - Daily at noon UTC
- `0 9 * * 1-5` - Weekdays at 9 AM UTC

### Change Output Filename
Edit `extract_dmv_wait_times.py` and modify the `save_to_json()` call in the `main()` function.

## Next Steps

- Add data visualization or analysis scripts
- Create a GitHub Pages site to display the data
- Set up notifications for specific wait time thresholds
- Add historical data tracking and trends
