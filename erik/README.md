## Recommended: Use python3.6 or higher
## Changes I made:
1. Put the kv code for each screen in a separate kv file
2. Removed the calls to `super().__init__()` in the python code for both of the screens (I believe that was needed if you were using python2e)
3. Added a .py and .kv file for your main screen
4. Removed the `build` function in your `MainApp` class in `main.py` in favor of creating the `ScreenManager` directly in `main.kv`
4. Added 
```
#:include screens/receivescreen.kv
#:include screens/sendscreen.kv
#:include screens/mainscreen.kv
```
into the `main.kv` file.
