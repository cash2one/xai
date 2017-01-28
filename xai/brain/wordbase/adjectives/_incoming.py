

#calss header
class _INCOMING():
	def __init__(self,): 
		self.name = "INCOMING"
		self.definitions = [u'arriving at or coming towards a place: ', u'soon to start something such as a job because recently chosen or elected: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
