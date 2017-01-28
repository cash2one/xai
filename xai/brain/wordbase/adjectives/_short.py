

#calss header
class _SHORT():
	def __init__(self,): 
		self.name = "SHORT"
		self.definitions = [u'small in length, distance, or height: ', u'used to say that a name is used as a shorter form of another name: ', u'being an amount of time that is less than average or usual: ', u'Short books, letters, and other examples of writing do not contain many words and do not take much time to read: ', u'to not have enough of something: ', u'unable to breathe very well, for example because you have been running or doing some type of energetic exercise: ', u'to be few or not enough in number: ', u'to not have something, especially when it is something you need in order to live: ', u'saying little but showing slight impatience or anger in the few words that you say: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
