import os
import logging
from dotenv import load_dotenv
from supabase.client import create_client

load_dotenv()


class SupabaseClient:
    """
    Singleton Pattern: using a single instance of the Supabase
    client throughout the application, implementing the Singleton pattern can
    be beneficial. This ensures that only one instance of the SupabaseClient
    exists in the application at any time, reducing resource usage and avoiding
    potential conflicts with multiple connections.
    """
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(SupabaseClient, cls).__new__(cls)
            try:
                url = os.getenv("SUPABASE_URL")
                key = os.getenv("SUPABASE_KEY")
                if not url or not key:
                    raise ValueError("Supabase URL or Key is missing.")
                cls._instance.supabase = create_client(url, key)
            except Exception as e:
                logging.error(f"Failed to create Supabase client: {e}")
                raise
        return cls._instance

    @property
    def client(self):
        return self._instance.supabase
