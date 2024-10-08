<script>
    import { isLoggedIn } from '../stores';
    import { writable } from 'svelte/store';
  
    let showLoginModal = writable(false);
    let username = '';
    let password = '';
  
    async function handleLogin() {
      try {
        const response = await fetch('http://localhost:8000/login', {
          method: 'POST',
          headers: { 'Content-Type': 'application/json' },
          body: JSON.stringify({ username, password })
        });
  
        if (response.ok) {
          isLoggedIn.set(true);
          showLoginModal.set(false);
        } else {
          console.error('Failed to log in');
        }
      } catch (error) {
        console.error('Error logging in:', error);
      }
    }
  </script>
  
  <style>
    @import 'bulma/css/bulma.css';
  
    .login-modal {
      display: none;
      position: absolute;
      right: 0;
      top: 100%;
      background: white;
      padding: 1rem;
      box-shadow: 0 2px 8px rgba(0, 0, 0, 0.15);
    }
  
    .navbar-item:hover .login-modal {
      display: block;
    }
  </style>
  
  <nav class="navbar" role="navigation" aria-label="main navigation">
    <div class="navbar-brand">
      <a class="navbar-item" href="#">
        Academic Documentation Center
      </a>
    </div>
  
    <div id="navbarBasicExample" class="navbar-menu">
      <div class="navbar-end">
        <div class="navbar-item" on:mouseover={() => showLoginModal.set(true)} on:mouseleave={() => showLoginModal.set(false)}>
          <div class="buttons">
            {#if !$isLoggedIn}
              <a class="button is-primary">
                <strong>Login</strong>
              </a>
              <div class="login-modal">
                <div class="field">
                  <label class="label">Username</label>
                  <div class="control">
                    <input class="input" type="text" bind:value={username} placeholder="Enter username">
                  </div>
                </div>
  
                <div class="field">
                  <label class="label">Password</label>
                  <div class="control">
                    <input class="input" type="password" bind:value={password} placeholder="Enter password">
                  </div>
                </div>
  
                <div class="control">
                  <button class="button is-link" on:click={handleLogin}>Login</button>
                </div>
              </div>
            {/if}
          </div>
        </div>
      </div>
    </div>
  </nav>  