# Expense Tracker - Personal Finance Management App

A modern, professional expense tracking web application built with Next.js 14, TypeScript, and Tailwind CSS. Track your expenses, visualize spending patterns, and manage your personal finances with ease.

## Features

### Core Functionality
- **Expense Management**: Add, edit, and delete expenses with ease
- **Smart Categorization**: Organize expenses into 6 categories (Food, Transportation, Entertainment, Shopping, Bills, Other)
- **Advanced Filtering**: Filter expenses by date range, category, and search query
- **Data Persistence**: All data saved locally using browser localStorage
- **Export Functionality**: Export your expenses to CSV for external analysis

### Dashboard & Analytics
- **Real-time Summary Cards**: View total spending, monthly spending, average expense, and total count
- **Category Breakdown**: Visual representation of spending across categories
- **Top Category Insights**: Identify your highest spending category at a glance

### User Experience
- **Modern, Clean Design**: Professional interface with intuitive navigation
- **Responsive Layout**: Seamless experience on desktop, tablet, and mobile devices
- **Form Validation**: Real-time validation ensures data integrity
- **Loading States**: Visual feedback during data operations
- **Accessible**: Keyboard navigation and focus states for better accessibility

## Tech Stack

- **Framework**: Next.js 14 (App Router)
- **Language**: TypeScript
- **Styling**: Tailwind CSS
- **Date Management**: date-fns
- **Data Storage**: Browser localStorage

## Getting Started

### Prerequisites

- Node.js 18.x or higher
- npm or yarn package manager

### Installation

1. **Clone or navigate to the project directory**:
   ```bash
   cd expense-tracker-ai
   ```

2. **Install dependencies**:
   ```bash
   npm install
   ```

3. **Run the development server**:
   ```bash
   npm run dev
   ```

4. **Open your browser**:
   Navigate to [http://localhost:3000](http://localhost:3000)

### Building for Production

```bash
npm run build
npm start
```

## Usage Guide

### Adding an Expense

1. Navigate to the **Dashboard** or **Expenses** page
2. Fill out the expense form:
   - **Date**: Select the date of the expense (defaults to today)
   - **Amount**: Enter the expense amount in dollars
   - **Category**: Choose from 6 categories
   - **Description**: Provide a brief description (minimum 3 characters)
3. Click **Add Expense** to save

### Viewing and Managing Expenses

1. Go to the **Expenses** page
2. Use the filters to narrow down expenses:
   - Search by description
   - Filter by category
   - Set date range (start and end dates)
3. Click **Edit** to modify an expense
4. Click **Delete** to remove an expense (with confirmation)

### Exporting Data

1. Navigate to the **Expenses** page
2. Apply any filters if needed
3. Click the **Export CSV** button
4. Your filtered expenses will be downloaded as a CSV file

### Dashboard Analytics

The dashboard provides:
- **Total Spending**: All-time total of expenses
- **Monthly Spending**: Total for the current month
- **Average Expense**: Mean expense amount
- **Total Expenses**: Count of all expenses
- **Category Breakdown**: Visual chart showing spending by category
- **Top Category**: Highest spending category with percentage

## Project Structure

```
expense-tracker-ai/
├── app/                    # Next.js app directory
│   ├── expenses/          # Expenses page
│   ├── layout.tsx         # Root layout
│   ├── page.tsx           # Dashboard page
│   └── globals.css        # Global styles
├── components/            # React components
│   ├── ui/               # Reusable UI components
│   │   ├── Button.tsx
│   │   ├── Card.tsx
│   │   ├── Input.tsx
│   │   ├── Select.tsx
│   │   ├── LoadingSpinner.tsx
│   │   └── Toast.tsx
│   ├── Navigation.tsx
│   ├── ExpenseForm.tsx
│   ├── ExpenseFilters.tsx
│   ├── ExpenseListItem.tsx
│   ├── SummaryCard.tsx
│   └── CategoryChart.tsx
├── lib/                   # Utility functions
│   ├── storage.ts        # localStorage utilities
│   └── analytics.ts      # Analytics and calculations
├── types/                 # TypeScript type definitions
│   └── expense.ts
└── public/               # Static assets
```

## Data Storage

All expense data is stored in your browser's localStorage under the key `expense-tracker-expenses`. This means:

- ✅ No backend required
- ✅ Data persists across sessions
- ✅ Complete privacy (data never leaves your device)
- ⚠️ Data is browser-specific (not synced across devices)
- ⚠️ Clearing browser data will delete expenses

## Browser Compatibility

- Chrome/Edge: 90+
- Firefox: 88+
- Safari: 14+
- Opera: 76+

## Development Scripts

```bash
# Run development server
npm run dev

# Build for production
npm run build

# Start production server
npm start

# Run linting
npm run lint
```

## Customization

### Adding New Categories

Edit `types/expense.ts`:
```typescript
export const CATEGORIES: Category[] = [
  'Food',
  'Transportation',
  'YourNewCategory',
  // ...
];
```

### Changing Currency

Edit `lib/analytics.ts` in the `formatCurrency` function:
```typescript
currency: 'EUR', // Change from 'USD'
```

### Modifying Color Scheme

Edit `tailwind.config.ts` to customize the color palette.

## Future Enhancements

Potential features for future versions:
- Cloud sync with backend database
- Recurring expenses
- Budget tracking and alerts
- Advanced charts and reporting
- Multiple currency support
- Receipt image uploads
- Dark mode toggle
- Data import from CSV/Excel

## License

This project is open source and available for personal and educational use.

## Support

For issues or questions, please open an issue in the repository.

---

Built with ❤️ using Next.js, TypeScript, and Tailwind CSS
