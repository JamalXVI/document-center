// Utility for handling user login
import { isLoggedIn, toast } from '../stores';

export async function handleLogin(username, password) {
  try {
    const response = await fetch('http://localhost:8000/login', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ username, password })
    });

    if (response.ok) {
      isLoggedIn.set(true);
      return true;
    } else {
      toast.set({ show: true, message: 'Failed to log in' });
      return false;
    }
  } catch (error) {
    toast.set({ show: true, message: 'Error logging in' });
    return false;
  }
}
