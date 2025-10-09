document.addEventListener('DOMContentLoaded', () => {
    const budgetForm = document.getElementById('budget-form');
    const incomeInput = document.getElementById('income');
    const expenseInput = document.getElementById('expense');
    const amountInput = document.getElementById('amount');
    const totalIncome = document.getElementById('total-income');
    const totalExpenses = document.getElementById('total-expenses');
    const remainingBalance = document.getElementById('remaining-balance');
    const expenseList = document.getElementById('expense-list');

    let income = 0;
    let expenses = 0;

    budgetForm.addEventListener('submit', (e) => {
        e.preventDefault();

        const expenseDescription = expenseInput.value;
        const expenseAmount = parseFloat(amountInput.value);

        if (income === 0) {
            income = parseFloat(incomeInput.value);
            totalIncome.textContent = income.toFixed(2);
        }

        expenses += expenseAmount;
        totalExpenses.textContent = expenses.toFixed(2);
        remainingBalance.textContent = (income - expenses).toFixed(2);

        const expenseItem = document.createElement('li');
        expenseItem.textContent = `${expenseDescription}: $${expenseAmount.toFixed(2)}`;
        expenseList.appendChild(expenseItem);

        expenseInput.value = '';
        amountInput.value = '';
    });
});