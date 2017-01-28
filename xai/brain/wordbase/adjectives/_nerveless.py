

#calss header
class _NERVELESS():
	def __init__(self,): 
		self.name = "NERVELESS"
		self.definitions = [u'calm and confident about something difficult that you are doing']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
