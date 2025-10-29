# Quick Start Guide

Get your Expense Tracker running in 3 simple steps!

## 🚀 Start the Application

```bash
npm run dev
```

Then open [http://localhost:3000](http://localhost:3000) in your browser.

## 📝 Try These Features

### 1. Add Your First Expense
1. On the **Dashboard** page, you'll see the expense form
2. Fill in:
   - Date: Today (pre-filled)
   - Amount: Try `25.50`
   - Category: Select "Food"
   - Description: "Lunch at cafe"
3. Click **Add Expense**

### 2. View Your Expenses
1. Click **Expenses** in the navigation
2. See your expense listed with all details
3. Try the filters:
   - Search for "lunch"
   - Filter by "Food" category
   - Set a date range

### 3. Edit or Delete
1. Click **Edit** on any expense
2. Modify the details
3. Click **Update Expense**
4. Or click **Delete** to remove it (with confirmation)

### 4. Export Your Data
1. Go to the **Expenses** page
2. Click **Export CSV** button
3. Open the downloaded file in Excel or Google Sheets

### 5. Explore the Dashboard
1. Return to the **Dashboard**
2. See your summary cards update automatically
3. View the category breakdown chart
4. Check your top spending category

## 🎨 Test the Responsive Design

1. Open your browser's developer tools (F12)
2. Toggle device toolbar (Ctrl+Shift+M or Cmd+Shift+M)
3. Try different screen sizes:
   - Mobile (375px)
   - Tablet (768px)
   - Desktop (1920px)

## 💡 Pro Tips

- **Keyboard Navigation**: Use Tab to navigate through form fields
- **Quick Add**: The form resets after adding an expense for quick entry
- **Data Safety**: Your data is saved automatically in localStorage
- **No Limits**: Add as many expenses as you need

## 🧪 Sample Data to Test With

Try adding these sample expenses:

1. **Morning Coffee**
   - Date: Today
   - Amount: $5.50
   - Category: Food
   - Description: "Daily coffee at Starbucks"

2. **Gas**
   - Date: Today
   - Amount: $45.00
   - Category: Transportation
   - Description: "Fill up car tank"

3. **Movie Tickets**
   - Date: Yesterday
   - Amount: $28.00
   - Category: Entertainment
   - Description: "Movie night with friends"

4. **Grocery Shopping**
   - Date: 3 days ago
   - Amount: $125.30
   - Category: Food
   - Description: "Weekly grocery shopping"

5. **Electric Bill**
   - Date: Last week
   - Amount: $85.00
   - Category: Bills
   - Description: "Monthly electricity bill"

## 🔍 Validation Testing

Try these to test form validation:

- Leave amount empty → See error message
- Enter negative amount → See validation error
- Leave description empty → Required field error
- Enter description with less than 3 characters → Minimum length error

## 🎯 All Features Checklist

- [ ] Add a new expense
- [ ] View expenses list
- [ ] Edit an existing expense
- [ ] Delete an expense
- [ ] Filter by category
- [ ] Search by description
- [ ] Filter by date range
- [ ] Export to CSV
- [ ] View dashboard analytics
- [ ] Check category breakdown
- [ ] Test on mobile view
- [ ] Test form validation

---

Enjoy tracking your expenses! 💰
