

#calss header
class _WORKMANLIKE():
	def __init__(self,): 
		self.name = "WORKMANLIKE"
		self.definitions = [u'showing an acceptable level of skill but no great ability or style: ', u'skilful: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
