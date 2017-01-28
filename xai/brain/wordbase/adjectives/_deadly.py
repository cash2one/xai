

#calss header
class _DEADLY():
	def __init__(self,): 
		self.name = "DEADLY"
		self.definitions = [u'likely to cause death: ', u'complete or extreme: ', u'extremely boring: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
