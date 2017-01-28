

#calss header
class _GAY():
	def __init__(self,): 
		self.name = "GAY"
		self.definitions = [u'sexually attracted to people of the same sex and not to people of the opposite sex: ', u'happy: ', u'If a place is gay, it is bright and attractive: ', u'not good, reasonable, or suitable']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
