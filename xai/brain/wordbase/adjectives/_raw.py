

#calss header
class _RAW():
	def __init__(self,): 
		self.name = "RAW"
		self.definitions = [u'(of food) not cooked: ', u'(of materials) in a natural state, without having been through any chemical or industrial process: ', u'Raw information has been collected but has not yet been studied in detail: ', u'used to refer to a person who is not trained or is without experience: ', u'Feelings or qualities that are raw are natural and difficult to control: ', u'A piece of writing that is raw is one that does not try to hide anything about its subject: ', u'sore or painful because of being rubbed or damaged: ', u'used to describe weather that is very cold: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
