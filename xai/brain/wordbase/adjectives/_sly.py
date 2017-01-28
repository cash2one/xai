

#calss header
class _SLY():
	def __init__(self,): 
		self.name = "SLY"
		self.definitions = [u'deceiving people in a clever way in order to get what you want: ', u'seeming to know secrets: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
