

#calss header
class _INVASIVE():
	def __init__(self,): 
		self.name = "INVASIVE"
		self.definitions = [u'moving into all areas of something and difficult to stop: ', u'An invasive organism is one that has arrived in a place from somewhere else and has a harmful effect on that place: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
