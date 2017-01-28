

#calss header
class _ATTENDANT():
	def __init__(self,): 
		self.name = "ATTENDANT"
		self.definitions = [u'coming with a stated thing or resulting from it: ', u'present with someone to help them, or present at an event, place, etc.: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
