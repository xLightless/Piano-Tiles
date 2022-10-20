from game import App
                
app = App()

if __name__ == "__main__":
    try:
        app.run(debug = False)
    except KeyboardInterrupt:
        pass