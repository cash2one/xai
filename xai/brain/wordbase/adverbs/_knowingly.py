

#calss header
class _KNOWINGLY():
	def __init__(self,): 
		self.name = "KNOWINGLY"
		self.definitions = [u'in a way that shows you know about something: ', u'If you do something knowingly, you do it knowing what will be its likely effect: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adverbs'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
