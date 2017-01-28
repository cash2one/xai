

#calss header
class _INJURED():
	def __init__(self,): 
		self.name = "INJURED"
		self.definitions = [u'hurt or physically harmed: ', u'If your feelings are injured, someone has offended or upset you: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
