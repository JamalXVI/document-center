<!-- Svelte-based Toast Component -->
<script>
    import { toast } from '../stores';
  
    let show = false;
    let message = '';
  
    toast.subscribe(value => {
      show = value.show;
      message = value.message;
  
      if (show) {
        setTimeout(() => {
          toast.set({ show: false, message: '' });
        }, 3000); // Hide toast after 3 seconds
      }
    });
  </script>
  
  <style>
    @import 'bulma/css/bulma.css';
  
    .toast {
      position: fixed;
      bottom: 20px;
      right: 20px;
      background: #323232;
      color: #fff;
      padding: 1rem;
      border-radius: 5px;
      box-shadow: 0 2px 8px rgba(0, 0, 0, 0.15);
      opacity: 0.9;
    }
  
    .toast-hidden {
      display: none;
    }
  </style>
  
  <div class:toast-hidden={!show} class="toast">
    {message}
  </div>
  