

#calss header
class _FINAL():
	def __init__(self,): 
		self.name = "FINAL"
		self.definitions = [u'last: ', u'used when you are talking about what is most important or true in a situation: ', u'used to show that you are certain you will not change your decision about something: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
