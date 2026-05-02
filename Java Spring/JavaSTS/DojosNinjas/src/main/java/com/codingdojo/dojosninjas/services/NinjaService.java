package com.codingdojo.dojosninjas.services;

import java.util.List;
import java.util.Optional;

import org.springframework.stereotype.Service;

import com.codingdojo.dojosninjas.models.Ninja;
import com.codingdojo.dojosninjas.repositories.NinjaRepository;

@Service
public class NinjaService {
	private final NinjaRepository nRepo;
	
	public NinjaService(NinjaRepository nRepo) {
		this.nRepo = nRepo;
	}
	
	public List<Ninja> findAll() {
        return nRepo.findAll();
    }
	
	public Ninja createNinja(Ninja n) {
		return nRepo.save(n);
	}
	
	public Ninja findOne(Long id) {
		Optional<Ninja> optionalNinja = nRepo.findById(id);
        if(optionalNinja.isPresent()) {
            return optionalNinja.get();
        } else {
            return null;
        }
	}
	
	public Ninja update(Ninja ninja) {
		Optional<Ninja> optionalNinja = nRepo.findById(ninja.getId());
		if(optionalNinja.isPresent()) {
			return nRepo.save(ninja);
		} else {
	    	return null;
		}
    }
    
    public void delete(Long id) {
		Optional<Ninja> optionalNinja = nRepo.findById(id);
		if(optionalNinja.isPresent()) {
			Ninja ninja = optionalNinja.get();
			nRepo.delete(ninja);
		}
    }
}
