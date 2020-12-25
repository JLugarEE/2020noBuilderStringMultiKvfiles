## Recommended: Use python3.6 or higher
## Changes I made:
1. Put the kv code for each screen in a separate kv file
2. Removed the calls to `super().__init__()` in the python code for both of the screens (I believe that was needed if you were using python2e)
3. Added 
```
#:include screens/receivescreen.kv
#:include screens/sendscreen.kv
```

into the `main.kv` file.
