import nlpcloud



class NLPApp:

  def __init__(self):
    self.__database={}
    self.__first_menu()

  def __first_menu(self):
    first_input=input("""
    hi how would you like to proceed?
    1. Not a mamber ? Register
    2. Already a member? Login.
    3. Galti sa agya.\n""")
    if first_input=='1':
      self.__register()
    elif first_input=='2':
      self.__login()
    else:
      exit()

  def __second_menu(self):
       second_input=input("""
       hi how would you like to proceed?
       1. NER
       2. Language Detection
       3. Sentiment Analysis
       4. logout\n""")
       if second_input=='1':
          self.__NER()
       elif second_input=='2':
          self.__Language_detection()
       elif second_input=='3':
          self.__Sentiment_analysis()
       else:
          self.__login()

  def __register(self):
    print('Register')
    name=input('Enter Name : ')
    email=input('Enter Email : ')
    password=input('Enter password : ')

    if email in self.__database :
      print('Email alredy exist !')
    else :
      self.__database[email]=[name,password]
      print('Registration Succcessful, Now Login \n')
      print(self.__database)
      self.__first_menu()
    #   self.__login()

  def __login(self):
    print('login')
    email=input('Enter Your email : ')
    password=input('Enter password : ')
    if email in self.__database:
      if password==self.__database[email][1]:
        print('Login Succesfull')
        self.__second_menu()
      else:
        print('Wrong Password !')
        self.__login()
    else:
      print('Email not register !')
      self.__register()

  def __NER(self):
      print('NER')

    #   para=input('Enter the paragraphe : ')
    #   search_term=input('What would you like to search : ')
    #   # NLP cloud work my api key not work
    #   api_key="2d58d7fb9af09e617ee525e78c7766b6d8c5bb61"
    #   client = nlpcloud.Client("finetuned-llama-2-70b",api_key , gpu=True)
    #   responce=client.entities(para,searched_entity=search_term)
    #   print(responce)

      self.__second_menu()

    
  def __Language_detection(self):
      print('Language Detection')

      # language_detection code heare

      self.__second_menu()

  def __Sentiment_analysis(self):
      print('Sentiment analysis')

    #   client = nlpcloud.Client("distilbert-base-uncased-emotion", "2d58d7fb9af09e617ee525e78c7766b6d8c5bb61", gpu=False)
    #   responce=client.sentiment("""Look what's just come on the market in #ValThorens! A recently renovated, charming 6 
    #   bed duplex apartment in the heart of the resort with superb views!""")
    #   print(responce)

      self.__second_menu()



obj=NLPApp()