

#calss header
class _HARD():
	def __init__(self,): 
		self.name = "HARD"
		self.definitions = [u'not easy to bend, cut, or break: ', u'difficult to understand, do, experience, or deal with: ', u'needing or using a lot of physical or mental effort: ', u'not pleasant or gentle; severe: ', u'to criticize someone severely, or to treat someone unfairly: ', u'A hard drink contains a high level of alcohol: ', u'Hard water contains a high level of minerals that prevent soap from cleaning.', u'able to be proved: ', u'used to describe a time when there is bad weather: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
