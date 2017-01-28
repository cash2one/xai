

#calss header
class _DAPPLED():
	def __init__(self,): 
		self.name = "DAPPLED"
		self.definitions = [u'covered with spots of colour that are lighter or darker than the main colour, or covered with areas of light and darkness: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
