

#calss header
class _PRESENTLY():
	def __init__(self,): 
		self.name = "PRESENTLY"
		self.definitions = [u'now; at the present time: ', u'soon; not at the present time but in the future, after a short time: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adverbs'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
