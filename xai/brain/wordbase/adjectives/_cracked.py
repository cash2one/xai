

#calss header
class _CRACKED():
	def __init__(self,): 
		self.name = "CRACKED"
		self.definitions = [u'If something is cracked, it is damaged with one or more thin lines on its surface: ', u'silly, stupid, or slightly mentally ill']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
