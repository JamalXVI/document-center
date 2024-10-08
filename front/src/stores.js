// Svelte store for global variables
import { writable } from 'svelte/store';

// API URL for the backend
export const apiUrl = writable('http://localhost:8000');

// Authentication status (logged in or not)
export const isLoggedIn = writable(false);
