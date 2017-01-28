

#calss header
class _STRAITENED():
	def __init__(self,): 
		self.name = "STRAITENED"
		self.definitions = [u'A straitened situation is difficult because there is much less money available to you than there was in the past: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
