package com.codingdojo.jpa.services;

import java.util.List;
import java.util.Optional;

import org.springframework.stereotype.Service;

import com.codingdojo.jpa.models.Book;
import com.codingdojo.jpa.repositories.BookRepository;

// Services are the business logic (DRY code) - slim controller and larger models

@Service
public class BookService {
    // adding the book repository as a dependency
    private final BookRepository bookRepository;
    
    public BookService(BookRepository bookRepository) {
        this.bookRepository = bookRepository;
    }
    // returns all the books
    public List<Book> allBooks() {
        return bookRepository.findAll();
    }
    // creates a book
    public Book createBook(Book b) {
        return bookRepository.save(b);
    }
    // retrieves a book
    public Book findBook(Long id) {
        Optional<Book> optionalBook = bookRepository.findById(id);
        if(optionalBook.isPresent()) {
            return optionalBook.get();
        } else {
            return null;
        }
    }
    
    // updates a book
    public Book updateBook(Book b) {
    	return bookRepository.save(b);
    }
    
    // return any books containing the search term in its description
    public List<Book> booksContaining(String search) {
    	return bookRepository.findByDescriptionContaining(search);
    }
}
