// Svelte store and API utility for fetching documents
import { writable } from 'svelte/store';
import { apiUrl } from '../stores';

export const documents = writable([]);

export async function fetchDocuments() {
  try {
    const response = await fetch(`${apiUrl}/documents`);
    if (!response.ok) {
      throw new Error('Failed to fetch documents');
    }
    const data = await response.json();
    documents.set(data);
  } catch (error) {
    console.error('Error fetching documents:', error);
  }
}

// Call this function in a Svelte component using `onMount`
// to initialize the document data when the component is mounted.