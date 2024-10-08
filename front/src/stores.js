import { writable } from 'svelte/store';

// API URL for the backend
export const apiUrl = writable('http://localhost:8000');

// Authentication status (logged in or not)
export const isLoggedIn = writable(false);

// Toast for displaying messages globally
export const toast = writable({ show: false, message: '' });
