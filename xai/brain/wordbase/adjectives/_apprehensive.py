

#calss header
class _APPREHENSIVE():
	def __init__(self,): 
		self.name = "APPREHENSIVE"
		self.definitions = [u'feeling worried about something that you are going to do or that is going to happen: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
