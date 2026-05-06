package com.codingdojo.safetravels.services;

import java.util.List;
import java.util.Optional;

import org.springframework.stereotype.Service;

import com.codingdojo.safetravels.models.Expense;
import com.codingdojo.safetravels.repositories.ExpenseRepository;

@Service
public class ExpenseService {
	// adds Expense Repository as dependency
	private final ExpenseRepository expenseRepository;
	// can name it whatever you need or shorter
	// left explicit as possible so easier to reference
	
	public ExpenseService(ExpenseRepository expenseRepository) {
		this.expenseRepository = expenseRepository;
	}
	
	// all features below
	
	// finds all the expenses
	public List<Expense> allExpenses() {
		return expenseRepository.findAll();
	}
	
	// creates an expense
	public Expense createExpense(Expense exp) {
		return expenseRepository.save(exp);
	}
	
	// retrieves an expense
	public Expense findExpense(Long id) {
		Optional<Expense> optionalExpense = expenseRepository.findById(id);
		if (optionalExpense.isPresent()) {
			return optionalExpense.get();
		}
		return null;
	}
	
	public Expense updateExpense(Expense exp) {
		Optional<Expense> optionalExpense = expenseRepository.findById(exp.getId());
		if (optionalExpense.isPresent()) {
			return expenseRepository.save(exp);
		} else {
			return null;
		}
	}
	
	public void deleteExpense(Long id) {
		Optional<Expense> optionalExpense = expenseRepository.findById(id);
		if(optionalExpense.isPresent()) {
			Expense expense = optionalExpense.get();
			expenseRepository.delete(expense);
			//expenseRepository.deleteById(id);
			// void so we don't have to return anything in delete function
		}
	}
}
