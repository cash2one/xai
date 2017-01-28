

#calss header
class _OLD():
	def __init__(self,): 
		self.name = "OLD"
		self.definitions = [u'having lived or existed for many years: ', u'unsuitable because intended for older people: ', u"used to describe or ask about someone's age: ", u'from a period in the past: ', u'a language when it was in an early stage in its development', u'(especially of a friend) known for a long time: ', u"used before someone's name when you are referring to or talking to them, to show that you know that person well and like them: "]

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
