

#calss header
class _INTERVENING():
	def __init__(self,): 
		self.name = "INTERVENING"
		self.definitions = [u'happening between two times or between other events or activities: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
