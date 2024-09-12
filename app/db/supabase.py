import os
from supabase import create_client, Client

class SupabaseClient:
    _instance = None  # Class variable to hold the single instance of SupabaseClient

    def __new__(cls):
        """
        Ensure only one instance of SupabaseClient is created (Singleton pattern).
        """
        if cls._instance is None:
            cls._instance = super(SupabaseClient, cls).__new__(cls)
            cls._instance._initialize_client()
        return cls._instance

    def _initialize_client(self):
        """
        Initialise the Supabase client with URL and Key from environment variables.
        """
        url: str = os.environ.get("SUPABASE_URL")
        key: str = os.environ.get("SUPABASE_KEY")

        if not url or not key:
            raise ValueError("Supabase URL and Key must be set in environment variables.")

        self.client: Client = create_client(url, key)

    def get_client(self) -> Client:
        """
        Get the initialised Supabase client.
        """
        return self.client