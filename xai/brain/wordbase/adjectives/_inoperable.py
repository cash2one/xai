

#calss header
class _INOPERABLE():
	def __init__(self,): 
		self.name = "INOPERABLE"
		self.definitions = [u'If a tumour (= a growth) or other medical condition is inoperable, doctors are unable to remove or treat it with an operation.', u'If a system, plan, machine, etc. is inoperable, it cannot be done or made to work.']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
