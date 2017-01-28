

#calss header
class _DEVILISH():
	def __init__(self,): 
		self.name = "DEVILISH"
		self.definitions = [u'evil or morally bad: ', u'morally bad but in an attractive way: ', u'extremely difficult or clever : ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
