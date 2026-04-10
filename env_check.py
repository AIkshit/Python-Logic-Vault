import sys
import platform

def check_environment():
    print("--- 🚀 Python Environment Check ---")
    print(f"System: {platform.system()} {platform.release()}")
    print(f"Python Version: {sys.version}")
    
    # Check for core AI/ML libraries (even if not installed yet)
    libraries = ['numpy', 'pandas', 'sklearn', 'matplotlib']
    print("\n--- 🧠 AI/ML Library Status ---")
    
    for lib in libraries:
        try:
            __import__(lib)
            print(f"✅ {lib}: Installed")
        except ImportError:
            print(f"❌ {lib}: Not found (Pending installation)")

    print("\nEnvironment check complete. Ready to build.")

if __name__ == "__main__":
    check_environment()
